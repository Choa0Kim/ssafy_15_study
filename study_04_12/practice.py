import sys
import heapq

class BattleBot:
    def __init__(self):
        # 맵 데이터 및 상태 변수 설정
        self.grid = []
        self.heigh = 0
        self.width = 0

        # 현재 나의 상태
        self.my_pos = (-1, -1)  #(y, x)
        self.my_dir = 'U' # 기본으로 바라보는 방향
        self.my_shells = 0 # 일반포탄
        self.my_mega_shells = 0 #메가 포탄

        # 목표 상태
        self.target_pos = (-1, -1) # (y, x)

        # 보급 시설 및 암호
        self.cipher_text = "" # 서버로부터 받은 암호문

        # 방향 매핑(상하좌우)
        # y축은  위로갈수록 감소(-1), 아래로 갈수로 증가(+1)
        self.dir_map = {'U': (-1, 0), 'D':(1, 0), 'L': (0, -1), 'R': (0, 1)}
        self.reverse_map = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}

    def update_state(self, map_data, allies, enmies, codes):
        """
        서버로부터 받은 데이터를 봇의 내부 상태로 업데이트.
        딕셔너리 구조
        """    
        self.grid = map_data
        self.height = len(map_data)
        self.width = len(map_data[0]) if self.height > 0 else 0

        # 암호문 업데이트 (리스트 형태로 들어오면 첫번 째 값 사용)
        self.cipher_text = codes[0] if codes and len(codes) > 0 else ""

        #  아군 정보 파싱
        # allies 딕셔너리에서 내 탱크 정보 파싱 (보통 key가 'A' 또는 'M' 임)
        # 만약 key 이름을 정확히 모른다면, 딕셔너리의 첫 번째 값(value)을 가져옴
        if allies:
            my_info = list(allies.values())[0]  # 첫번째 아군 정보 추출
            # 템플릿 변수명이 다를 수 있음. 당일 터미널 출력을 보고 수정
            # ex. my_info['y']
            self.my_pos = (my_info.get('y', -1), my_info.get('x', -1))
            self.my_dir = my_info.get('dir', self.my_dir)
            # 일반 포탄/메가 포탄 key 이름이 'shells'가 아닐수도 있음.
            # ex. missiles
            self.my_shells = my_info.get('missiles', my_info.get('shells', 0))
            self.my_mega_shells = my_info.get('mega_missiles', my_info.get('mega_shells', 0))

        # enemies 딕셔너리에서 적 포탑(x) 정보 파싱
        if enmies:
            enemy_info = list(enmies.values(0))[0]
            self.target_pos = (enemy_info.get('y', -1), enemy_info.get('x', -1))

    def decode_cipher(self):
        if not self.cipher_text: return ""
        excepted_keywords = ["SSAFY", "BATTLE", "SAMSUNG", "ALGORITHM", "PASS", "TANK"]
        for shift in range(26):
            decoded_candidate = ""
            for char in self.cipher_text:
                if char.isupper():
                    decoded_candidate += chr((ord(char) - 65 - shift) % 26 + 65)
                else: decoded_candidate += char

            for keyword in excepted_keywords:
                if keyword in decoded_candidate: return decoded_candidate
            return self.cipher_text


    def get_distance(self, pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
        
    def has_clear_line_of_sight(self, start, target):
        sy, sx = start
        ty, tx = target

        obstacles = ['R', 'W', 'T']
        if sy == ty :
            for x in range(min(sx, tx)+1, max(sx, tx)):
                if self.grid[sy][x] in obstacles: return False
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

                

            

                


        
        

        
