import sys
import heapq
from collections import deque

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
        
        # 목표 상태
        self.target_pos = (-1, -1) # (y, x)
        
        # 보급 시설 및 암호
        self.cipher_text = ""      
        
        # 방향 매핑 (상, 하, 좌, 우)
        self.dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.reverse_dir_map = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

    def update_state(self, map_data, allies, enemies, codes):
        """
        [수정됨] 실제 SSAFY 템플릿의 딕셔너리 구조에 맞춰 파싱합니다.
        """
        self.grid = map_data
        self.height = len(map_data)
        self.width = len(map_data[0]) if self.height > 0 else 0
        
        # 암호문 업데이트 (리스트 형태로 들어오면 첫 번째 값 사용)
        self.cipher_text = codes[0] if codes and len(codes) > 0 else ""
        
        # [핵심] allies 딕셔너리에서 내 탱크 정보 파싱 (보통 key가 'A' 또는 'M'임)
        # 만약 key 이름을 정확히 모른다면, 딕셔너리의 첫 번째 값(value)을 가져옵니다.
        if allies:
            my_info = list(allies.values())[0] # 첫 번째 아군 정보 추출
            # 템플릿 변수명이 다를 수 있으니, 당일 터미널 출력 보고 수정하세요! (예: my_info['y'])
            self.my_pos = (my_info.get('y', -1), my_info.get('x', -1))
            self.my_dir = my_info.get('dir', self.my_dir) 
            # 일반 포탄/메가 포탄 key 이름은 'shells'가 아닐 수 있습니다 (예: 'missiles')
            self.my_shells = my_info.get('missiles', my_info.get('shells', 0))
            self.my_mega_shells = my_info.get('mega_missiles', my_info.get('mega_shells', 0))
            
        # [핵심] enemies 딕셔너리에서 적 포탑(X) 정보 파싱
        if enemies:
            enemy_info = list(enemies.values())[0]
            self.target_pos = (enemy_info.get('y', -1), enemy_info.get('x', -1))

    def decode_cipher(self):
        if not self.cipher_text: return ""
        expected_keywords = ["SSAFY", "BATTLE", "SAMSUNG", "ALGORITHM", "PASS", "TANK"]
        for shift in range(26):
            decoded_candidate = ""
            for char in self.cipher_text:
                if char.isupper():
                    decoded_candidate += chr((ord(char) - 65 - shift) % 26 + 65)
                else: decoded_candidate += char
            for keyword in expected_keywords:
                if keyword in decoded_candidate: return decoded_candidate
        return self.cipher_text

    def get_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def has_clear_line_of_sight(self, start, target):
        sy, sx = start
        ty, tx = target
        obstacles = ['R', 'W', 'T']
        if sy == ty:
            for x in range(min(sx, tx) + 1, max(sx, tx)):
                if self.grid[sy][x] in obstacles: return False
            return True
        elif sx == tx:
            for y in range(min(sy, ty) + 1, max(sy, ty)):
                if self.grid[y][sx] in obstacles: return False
            return True
        return False

    def find_path_dijkstra(self, start, target):
        if start == (-1, -1) or target == (-1, -1): return []
        pq = [(0, start[0], start[1], [])]
        distances = {start: 0}
        while pq:
            cost, y, x, path = heapq.heappop(pq)
            if cost > distances.get((y, x), float('inf')): continue
                
            dist = self.get_distance((y, x), target)
            if (y, x) == target or (dist <= 3 and (y == target[0] or x == target[1]) and self.has_clear_line_of_sight((y, x), target)):
                return path
            
            for dy, dx in self.dir_map.values():
                ny, nx = y + dy, x + dx
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    cell = self.grid[ny][nx]
                    if cell in ['G', 'S', 'F', 'X', 'M2', 'E1', 'E2'] or cell == self.grid[target[0]][target[1]]:
                        new_cost = cost + 1
                    elif cell == 'T' and (self.my_shells > 0 or self.my_mega_shells > 0):
                        new_cost = cost + 2
                    else: continue 

                    if new_cost < distances.get((ny, nx), float('inf')):
                        distances[(ny, nx)] = new_cost
                        heapq.heappush(pq, (new_cost, ny, nx, path + [(ny, nx)]))
        return []

    def get_action(self):
        if self.cipher_text:
            decoded = self.decode_cipher()
            self.cipher_text = "" 
            return f"G {decoded}"
            
        y, x = self.my_pos
        ty, tx = self.target_pos
        
        dist = self.get_distance(self.my_pos, self.target_pos)
        if dist <= 3 and (y == ty or x == tx) and self.has_clear_line_of_sight(self.my_pos, self.target_pos):
            target_dir = ''
            if y == ty: target_dir = 'R' if tx > x else 'L'
            elif x == tx: target_dir = 'D' if ty > y else 'U'
            
            if self.my_dir == target_dir: return "F M" if self.my_mega_shells > 0 else "F"
            else:
                self.my_dir = target_dir
                return target_dir

        path = self.find_path_dijkstra(self.my_pos, self.target_pos)
        if path and len(path) > 0:
            next_y, next_x = path[0]
            dy, dx = next_y - y, next_x - x
            needed_dir = self.reverse_dir_map[(dy, dx)]
            target_cell = self.grid[next_y][next_x]
            
            if target_cell == 'T':
                if self.my_dir == needed_dir: return "F M" if self.my_mega_shells > 0 else "F"
                else:
                    self.my_dir = needed_dir
                    return needed_dir
            else:
                if self.my_dir == needed_dir: return "A" 
                else:
                    self.my_dir = needed_dir
                    return f"{needed_dir} A" 
        return "S"
    

# ==========================================
# 실행 예시 (로컬 테스트 및 검증용)
# ==========================================
if __name__ == "__main__":
    bot = BattleBot()
    
    # [가상의 테스트 시나리오]
    # 맵 크기: 5x5
    # 내 위치: (0, 0) / 적 위치: (4, 0)
    # 상황: 나(0,0)와 적(4,0) 사이에 나무(T) 2개가 가로막고 있음.
    # 오른쪽으로 빙~ 돌아가는 길(G)이 있지만 턴이 훨씬 오래 걸림.
    test_map = [
        ['G', 'G', 'G', 'G', 'G'],
        ['T', 'R', 'R', 'R', 'G'],
        ['T', 'R', 'G', 'G', 'G'],
        ['G', 'R', 'G', 'R', 'R'],
        ['X', 'G', 'G', 'G', 'G']
    ]
    
    # 초기 상태: 아래(D)를 보고 있고, 메가 포탄 1개, 일반 포탄 1개를 가짐
    allies_data = {'A': {'id': 'A', 'y': 0, 'x': 0, 'dir': 'D', 'shells': 1, 'mega_shells': 1}}
    enemies_data = {'X': {'id': 'X', 'y': 4, 'x': 0}}
    test_codes = ["VUDDOHVVDIB"] # "BATTLESSAFY"를 3칸 밀어낸 암호문
    
    print("--- 턴 1: 맵 진입 및 암호 해독 최우선 처리 ---")
    bot.update_state(test_map, allies_data, enemies_data, test_codes)
    action1 = bot.get_action()
    print(f"제출할 커맨드 (예상: 암호 제출 G BATTLESSAFY): {action1}")
    
    print("\n--- 턴 2: 암호 제출 후, 지름길 개척(나무 파괴) 판단 ---")
    # 서버에 암호를 보냈으므로 이번 턴부터는 암호문이 안 들어옴
    bot.update_state(test_map, allies_data, enemies_data, codes=[])
    action2 = bot.get_action()
    print(f"제출할 커맨드 (예상: 나무를 향해 메가포탄 발사 F M): {action2}")
    
    print("\n--- 턴 3: 첫 번째 나무 파괴 후, 두 번째 나무 파괴 판단 ---")
    # 맵 갱신: 첫 번째 나무(1,0)가 파괴되어 평지(G)가 됨 / 메가 포탄 소진
    test_map[1][0] = 'G'
    allies_data['A']['mega_shells'] = 0
    bot.update_state(test_map, allies_data, enemies_data, codes=[])
    action3 = bot.get_action()
    print(f"제출할 커맨드 (예상: 다음 나무를 향해 일반포탄 발사 F): {action3}")
    
    print("\n--- 턴 4: 나무 모두 파괴 완료, 전진 ---")
    # 맵 갱신: 두 번째 나무(2,0) 파괴 완료 / 모든 포탄 소진
    test_map[2][0] = 'G'
    allies_data['A']['shells'] = 0
    bot.update_state(test_map, allies_data, enemies_data, codes=[])
    action4 = bot.get_action()
    print(f"제출할 커맨드 (예상: 평지로 전진 A): {action4}")
    
    print("\n--- 턴 5: 전진 완료 후 사거리(3) 내 진입 ➔ 적군 타격 ---")
    # 위치 갱신: 내 탱크가 한 칸 앞으로 전진하여 (1,0)에 도착함
    allies_data['A']['y'] = 1
    # 맵 상에서 포탄 1개를 새로 보급받았다고 가정
    allies_data['A']['shells'] = 1 
    bot.update_state(test_map, allies_data, enemies_data, codes=[])
    action5 = bot.get_action()
    print(f"제출할 커맨드 (예상: 적 포탑을 향해 사격 F): {action5}")