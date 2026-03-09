import sys 
sys.stdin = open("input.txt", "r")

from collections import deque


# N:세로 , M: 가로
# 바이러스는 상하좌우로 인접한 빈칸으로 퍼짐 => 상하좌우 델타배열
# 0: 빈칸, 1: 벽, 2: 바이러스

N, M = map(int, input().split())
# print(N, M)
mapp = [list(map(int, input().split())) for _ in range(N)]
# print(mapp)
visited = [[0]*M for _ in range(N)]

# 상하좌우 배열 지정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 3개의 벽을 세우는 모든 경우의 수를 돌면서 안전 영역의 크기를 확인
# 2. 한 경우의 수를 돌 때마다? 안정영역의 크기를 갱신

# 벽 세울 곳 탐색하는 함수
def bfs(start_x, start_y):
  # 큐 생성 및 시작점 지정
  queue = deque([(start_x, start_y)])
  # 시작점 방문처리
  visited[start_x][start_y] = 1
  




# 시작점 찾기(바이러스)
for i in range(N):
  for j in range(M):
    # 현재 위치가 2이고, 방문하지 않았다면
    if mapp[i][j] == 2 and visited[i][j] == 0:
      # 현재 위치를 시작점으로 벽을 세울 곳 탐색
      bfs(i, j)

      




