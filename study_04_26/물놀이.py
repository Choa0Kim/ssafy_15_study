# swea 10966

"""
모든 물('W')의 위치를 큐에 먼저 집어 넣고, 한 번에 BFS 시작헤서
땅('L')까지의 최단 거리를 구함
"""

from collections import deque
import sys 
sys.stdin = open("input.txt", "r")

def solve():
    
    T = int(input())

    for tc in range(1, T+1):
        N, M = map(int, input().split())
        grid = [input().strip() for _ in range(N)]
        
        # 각 칸까지의 최소 거리 저장 배열 (-1은 미방문 상태)
        dist = [[-1]* M for _ in range(N)]
        queue = deque()

        # 큐 초기화: 모든 물의 위치를 찾아 큐에 삽입하고 거리를 0으로 설정
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 'W':
                    queue.append((i, j))
                    dist[i][j] = 0
        # 4방향 탐색
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        ans = 0 # 모든 땅에서 물까지의 최소거리의 합

        # 다중 출발점 bfs 진행
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x +dx[i]
                ny = y+dy[i]

                # 범위 확인: 격자 범위 내에 있고, 아직 방문하지 않은 곳(-1)이라면 땅('L')임
                if 0 <= nx <N and 0 <= ny < M and dist[nx][ny] ==-1:
                    # 현재 위치까지의 거리에서 +1
                    dist[nx][ny] = dist[x][y] +1
                    
                    # 큐에 넣을 때 정답에 미리 누적해서 더해줌 (나중에 배열을 또 순회할 필요 없음)
                    ans += dist[nx][ny]
                    queue.append((nx, ny))
        print(f'#{tc} {ans}')

solve()                    
    



    
