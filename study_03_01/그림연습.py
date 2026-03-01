import sys
sys.stdin = open("input.txt", "r")

#deque 사용
from collections import deque

# 입력 받기 n:세로, m:가로, 그림:graph
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# print(n, m, graph)

# 방문기록
visited = [[0]*m for _ in range(n)]
# print(visited)

# 상하좌우 좌표 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수설정(그림 넓이 측정기)
# 받을 인자:현재 위치, 그래프, 가로, 세로
def bfs(start_x, start_y, graph, n, m):
    # 빈 deque만들기
    queue= deque()
    # deque 시작점(초기값) 설정
    queue = deque([(start_x, start_y)]) # 튜플인 이유는 1. append는 1개의 인자만 받을 수 있고, x,y를 같이 가야해서
    #시작점 방문 기록
    visited[start_x][start_y] = 1
    # 시작점 방문했으니 넓이는 1부터 시작
    area_size = 1
    # queue에 남아있는 죄표가 있을 때까지 탐색 시작
    while queue:
        # 큐에 가장 앞에 있는 좌표 꺼내와서 현재 좌표로
        x, y = queue.popleft()
        # 현재 좌표로 사방탐색
        for i in range(4):
            #다음에 갈 위치 지정
            nx = x + dx[i]
            ny = y + dy[i]
            #다음에 갈 위치가 범위 안에 있는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny]==1:
                    #범위안에 잇고, 방문기록도 없고 색칠되어 있는곳'1'이라면
                    # 방문기록
                    visited[nx][ny] = 1
                    #이 칸을 기준으로 주변을 탐색해야 하므로 큐에 집어 넣기
                    queue.append((nx, ny))
                    # 넓이 추가
                    area_size += 1
    # while문을 돌면서 한 그림의 넓이 반환
    return area_size 
cnt = 0  #그림 덩어리 갯수
max_area = 0  # 가장 큰 그림 덩어리의 넓이
# 메인루프(그림 탐색) 
# 좌표 접근
for i in range(n):
    for j in range(m):
        #1인 지점 찾기,그리고 방문 기록도 없는
        if graph[i][j] == 1 and visited[i][j] == 0:
            # 그림 시작점을 찾았다면 넓이 측정기 호출(bfs 함수)
            # 그리고 측정기의 결과값은 result에 저장
            result = bfs(i, j, graph, n, m)
            #측정기 돌리고 나서 그림 갯수 추가
            cnt +=1
            # result 최대값 확인
        if result > max_area:
            max_area = result
print(cnt)
print(max_area)                

                      
 


