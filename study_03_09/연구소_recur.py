# import sys 
# sys.stdin = open("input.txt", "r")

# from collections import deque


# # N:세로 , M: 가로
# # 바이러스는 상하좌우로 인접한 빈칸으로 퍼짐 => 상하좌우 델타배열
# # 0: 빈칸, 1: 벽, 2: 바이러스
# # dfs, bfs를 동시에 사용하는 문제
# # dfs로 벽을세우고 bfs로 바이러스  퍼뜨리는?

# N, M = map(int, input().split())
# # print(N, M)
# mapp = [list(map(int, input().split())) for _ in range(N)]
# # print(mapp)
# visited = [[0]*M for _ in range(N)]

# # 상하좌우 배열 지정
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # 1. 3개의 벽을 세우는 모든 경우의 수를 돌면서 안전 영역의 크기를 확인
# # 2. 한 경우의 수를 돌 때마다? 안정영역의 크기를 갱신

# # 벽 세울 곳 탐색하는 함수
# def bfs(start_x, start_y):
#   # 큐 생성 및 시작점 지정
#   queue = deque([(start_x, start_y)])
#   # 시작점 방문처리
#   visited[start_x][start_y] = 1
  


# #dfs벽 세우기


# # 시작점 찾기(바이러스)
# for i in range(N):
#   for j in range(M):
#     # 현재 위치가 2이고, 방문하지 않았다면
#     if mapp[i][j] == 2 and visited[i][j] == 0:
#       # 현재 위치를 시작점으로 벽을 세울 곳 탐색
#       bfs(i, j)


from collections import deque

# 세로 N , 가로 M
N, M = map(int, input().split())

# 연구소 배치 2차원 리스트
lab = [list(map(int, input().split())) for _ in range(N)]

# 델타 상,하,좌,우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 안전 영역의 최대 개수
safe_count = 0

# 빈 칸 리스트
# 벽을 세울 수 있거나, 바이러스가 퍼질 수 있는 통로
empty = [(y, x) for y in range(N) for x in range(M) if lab[y][x] == 0]

# 바이러스 좌표
virus = [(y, x) for y in range(N) for x in range(M) if lab[y][x] == 2]


# dfs 벽 세우기
# bfs 안전 영역 개수 세기
##################### DFS: 벽 3개 설치 ####################
def dfs(cnt, start):
    if cnt == 3:
        bfs()
        return
    
    for i in range(start, len(empty)):
        y, x = empty[i]
        lab[y][x] = 1
        dfs(cnt+1, i+1)
        lab[y][x] = 0


############### BFS: 벽 3개 세운 상태에서 안전 영역 계산 ###############
def bfs():
    q = deque()
    visited = [[0] * M for _ in range(N)]

    for y, x in virus:
        q.append((y, x))
        visited[y][x] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if lab[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))

    safe = 0
    for y in range(N):
        for x in range(M):
            if lab[y][x] == 0 and visited[y][x] == 0:
                safe += 1

    global safe_count
    safe_count = max(safe_count, safe)


# DFS 시작
dfs(0, 0)

# 결과 출력
print(safe_count)



      




