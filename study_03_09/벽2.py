import sys
sys.stdin = open("input.txt", "r")

from collections import deque

# n :가로 m:세로
N, M = map(int, input().split())
# print(N, M)
mapp = [list(map(int, input()))for _ in range(N)]
# print(mapp)
# 방문처리
visited = [[0]*M for _ in range(N)]
# 벽 안 뿌신 visited 만들어서 방문처리따로하기
# 벽 만나고 안 만나거 둘 다 visited 
# 상하좌우 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#최단거리 bfs
def bfs(start_x, start_y):
    # 큐 생성하고 시작점 넣기
    queue = deque([(start_x, start_y)])
    # 시작점 방문처리
    visited[start_x][start_y] = 1
    lenn = 0

    while queue:
        # 큐에서 가장 앞에 있는거 빼서 현재 좌표로 지정
        x, y = queue.popleft()
        # 현재 지점을 기준으로 상하좌우 탐색
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 유효범위
            if 0 <= next_x < N and 0 <= next_y < M:
                if mapp[next_x][next_y] == 0 and visited[next_x][next_y] == 0:
                    # 유효한 범위라면 방문처리
                    visited[next_x][next_y] =1
                    # 발자국 남기기
                    mapp[next_x][next_y] = mapp[x][y] +1
                    # 현재 위치를 다음 위치로 하기 위해 큐 넣기
                    queue.append((next_x, next_y))
    # 최단거리
    return mapp[N-1][M-1]  



#시작점은 1,1
print(bfs(1, 1))