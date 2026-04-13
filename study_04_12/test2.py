import sys
import heapq

class BattleBot:
    def __init__(self):
        # 맵 데이터 및 상태 변수
        self.grid = []
        self.height = 0
        self.width = 0
        
        # 내 상태
        self.my_pos = (-1, -1)     # (y, x)
        self.my_dir = 'U'          # 기본 바라보는 방향
        self.my_shells = 0         # 일반 포탄
        self.my_mega_shells = 0    # 메가 포탄
        
        # 목표 상태 (적 포탑 또는 탱크)
        self.target_pos = (-1, -1) # (y, x)
        
        # 보급 시설 및 암호
        self.cipher_text = ""      # 서버로부터 받은 암호문
        
        # 방향 매핑 (상, 하, 좌, 우) 
        # y축은 위로 갈수록 감소(-1), 아래로 갈수록 증가(+1)
        self.dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.reverse_dir_map= {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

    def update_state(self, map_data, allies, enemies, cipher_text=""):
        """
        서버로부터 받은 데이터를 봇의 내부 상태로 업데이트합니다.
        (딕셔너리 리스트 형태를 가정)
        """
        self.grid = map_data
        self.height = len(map_data)
        self.width = len(map_data[0]) if self.height > 0 else 0
        self.cipher_text = cipher_text
        
        # 아군 정보 파싱
        if allies and len(allies) > 0:
            me = allies[0]
            self.my_pos = (me.get('y', -1), me.get('x', -1))
            self.my_dir = me.get('dir', self.my_dir) 
            self.my_shells = me.get('shells', 0)
            self.my_mega_shells = me.get('mega_shells', 0)
            
        # 적군 정보 파싱
        if enemies and len(enemies) > 0:
            target = enemies[0]
            self.target_pos = (target.get('y', -1), target.get('x', -1))

    def decode_cipher(self):
        """
        [만능 카이사르 암호 해독기 - 브루트포스]
        0~25칸을 모두 밀어보고 예상 키워드가 포함된 문장을 반환합니다.
        """
        if not self.cipher_text:
            return ""
            
        # 예상 정답 키워드 (시험 당일 필요에 따라 추가하세요)
        expected_keywords = ["SSAFY", "BATTLE", "SAMSUNG", "ALGORITHM", "PASS", "TANK"]
        
        for shift in range(26):
            decoded_candidate = ""
            for char in self.cipher_text:
                if char.isupper():
                    decoded_candidate += chr((ord(char) - 65 - shift) % 26 + 65)
                else:
                    decoded_candidate += char
            
            for keyword in expected_keywords:
                if keyword in decoded_candidate:
                    return decoded_candidate
                    
        return self.cipher_text

    def get_distance(se lf, pos1, pos2):
        """ 맨해튼 거리 반환 """
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def has_clear_line_of_sight(self, start, target):
        """ 
        공격 시, 포탄이 날아가는 경로에 막히는 장애물이 있는지 확인합니다.
        포탄은 바위(R)에 막히며, 나무(T)가 있으면 나무가 맞으므로 타겟을 맞출 수 없습니다.
        (물(W)의 경우, 포탄이 위로 날아갈 수 없다면 리스트에 유지하고, 날아갈 수 있다면 제외하세요)
        """
        sy, sx = start
        ty, tx = target
        
        obstacles = ['R', 'W', 'T']
        
        if sy == ty: # 가로로 일직선
            min_x, max_x = min(sx, tx), max(sx, tx)
            for x in range(min_x + 1, max_x):
                if self.grid[sy][x] in obstacles:
                    return False
            return True
        elif sx == tx: # 세로로 일직선
            min_y, max_y = min(sy, ty), max(sy, ty)
            for y in range(min_y + 1, max_y):
                if self.grid[y][sx] in obstacles:
                    return False
            return True
        return False

    def find_path_dijkstra(self, start, target):
        """ 다익스트라(Dijkstra) 알고리즘: 나무(T) 파괴(가중치 2)를 고려한 최단거리 탐색 """
        if start == (-1, -1) or target == (-1, -1):
            return []
            
        # 큐 데이터 형태: (누적 소모 턴 수, y, x, 경로 리스트)
        pq = [(0, start[0], start[1], [])]
        distances = {start: 0}
        
        while pq:
            cost, y, x, path = heapq.heappop(pq)
            
            # 이미 기록된 최단 거리보다 현재 비용이 크면 스킵
            if cost > distances.get((y, x), float('inf')):
                continue
                
            # [목표 도착 조건] 거리가 3 이하, 일직선이며, 시야에 장애물이 없으면 타겟 사정권!
            dist = self.get_distance((y, x), target)
            if (y, x) == target or (dist <= 3 and (y == target[0] or x == target[1]) and self.has_clear_line_of_sight((y, x), target)):
                return path
            
            for dy, dx in self.dir_map.values():
                ny, nx = y + dy, x + dx
                
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    cell = self.grid[ny][nx]
                    
                    # 1. 일반 지형 이동 (풀, 모래, 보급시설, 기타 등) -> 1턴 소모
                    if cell in ['G', 'S', 'F', 'X', 'M2', 'E1', 'E2'] or cell == self.grid[target[0]][target[1]]:
                        new_cost = cost + 1
                        
                    # 2. 나무(T) 파괴 후 전진 (포탄이 1개 이상 있을 때만 가능) -> 2턴 소모
                    elif cell == 'T' and (self.my_shells > 0 or self.my_mega_shells > 0):
                        new_cost = cost + 2
                        
                    # 바위(R) 및 물(W)은 절대 통과 불가
                    else:
                        continue 

                    # 더 최단 턴 수를 찾았을 때만 큐에 추가
                    if new_cost < distances.get((ny, nx), float('inf')):
                        distances[(ny, nx)] = new_cost
                        heapq.heappush(pq, (new_cost, ny, nx, path + [(ny, nx)]))
        return []

    def get_action(self):
        """ 이번 턴에 실행할 명령(Action)을 결정하여 문자열로 반환 """
        
        # 1. 보급 시설(F) 암호 해독 판정 (가장 최우선 순위)
        if self.cipher_text:
            decoded = self.decode_cipher()
            self.cipher_text = "" # 한 번 해독하면 비움 (중복 제출 방지)
            return f"G {decoded}"
            
        y, x = self.my_pos
        ty, tx = self.target_pos
        
        # 2. 사거리 내 타겟 공격 판정
        dist = self.get_distance(self.my_pos, self.target_pos)
        if dist <= 3 and (y == ty or x == tx) and self.has_clear_line_of_sight(self.my_pos, self.target_pos):
            # 타겟 방향 계산
            target_dir = ''
            if y == ty: target_dir = 'R' if tx > x else 'L'
            elif x == tx: target_dir = 'D' if ty > y else 'U'
            
            # 이미 타겟을 향하고 있다면 발포
            if self.my_dir == target_dir:
                return "F M" if self.my_mega_shells > 0 else "F"
            # 향하고 있지 않다면 제자리 방향 전환
            else:
                self.my_dir = target_dir
                return target_dir

        # 3. 목표 지점을 향해 이동 (또는 장애물 파괴) 판정
        path = self.find_path_dijkstra(self.my_pos, self.target_pos)
        if path and len(path) > 0:
            next_y, next_x = path[0]
            dy, dx = next_y - y, next_x - x
            needed_dir = self.reverse_dir_map[(dy, dx)]
            
            target_cell = self.grid[next_y][next_x]
            
            # [특수] 다음 가야 할 칸이 길막 중인 '나무(T)' 라면
            if target_cell == 'T':
                if self.my_dir == needed_dir:
                    # 나무를 바라보고 있다면 바로 쏴서 파괴!
                    return "F M" if self.my_mega_shells > 0 else "F"
                else:
                    # 안 바라보고 있다면 나무 쪽으로 포신 회전
                    self.my_dir = needed_dir
                    return needed_dir

            # [일반] 가야 할 칸이 비어있는 타일이라면
            else:
                if self.my_dir == needed_dir:
                    return "A" # 전진
                else:
                    self.my_dir = needed_dir
                    return f"{needed_dir} A" # 회전 후 전진
                
        # 예외: 경로가 없거나 행동이 불가능한 상태
        return "S"


# ==========================================
# 실행 예시 (로컬 테스트 및 검증용)
# ==========================================
if __name__ == "__main__":
    bot = BattleBot()
    
    # 가상의 테스트 환경
    # 내 앞(y=1)에 부술 수 있는 나무(T)가 있고 목표(X)가 건너편(y=2)에 위치함
    test_map = [
        ['G', 'R', 'G', 'G', 'G'],
        ['T', 'W', 'W', 'W', 'G'],
        ['X', 'R', 'G', 'G', 'G'],
        ['G', 'G', 'G', 'G', 'G']
    ]
    
    # 나는 (0, 0)에 있고 아래(D)를 바라보며 포탄 1개를 가짐
    allies_data = [{'id': 'M1', 'y': 0, 'x': 0, 'dir': 'D', 'shells': 1, 'mega_shells': 0}]
    enemies_data = [{'id': 'X1', 'y': 2, 'x': 0}]
    
    print("--- 턴 1: 데이터 업데이트 ---")
    bot.update_state(test_map, allies_data, enemies_data)
    
    action1 = bot.get_action()
    print(f"제출할 커맨드 (예상: 나무를 향해 발포 F): {action1}")
    
    # 턴 2: 나무가 부서져 평지(G)가 되었다고 가정하고 업데이트
    print("\n--- 턴 2: 나무 파괴 후 평지(G)로 데이터 갱신 ---")
    test_map[1][0] = 'G'
    bot.my_shells = 0
    bot.update_state(test_map, allies_data, enemies_data)
    
    action2 = bot.get_action()
    print(f"제출할 커맨드 (예상: 평지로 전진 A): {action2}")