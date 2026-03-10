from itertools import combinations
from collections import deque

def bfs(li):
    global total
    for i in range(3):
        road[li[i][0]][li[i][1]] = 1
    
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if road[i][j] == 1:
                visited[i][j] = True
    
    que = deque()
    for i in virus:
        que.append(i)
        visited[i[0]][i[1]] = True
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if 0<= dx < N and 0 <= dy < M:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    que.append((dx, dy))
    
    summ = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                summ += 1
    
    if summ > total:
        total = summ
    


    for i in range(3):
        road[li[i][0]][li[i][1]] = 0


N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
nowall = [] 
virus = []

for i in range(N):
    for j in range(M):
        if road[i][j] == 0:
            nowall.append((i,j))
        if road[i][j] == 2:
            virus.append((i,j))

di = [1,0,-1,0]
dj = [0,1,0,-1]

# 0 다 찾아서 리스트에 다 넣어서 콤비 돌림.(원하는 리스트, 몇개 조합으로 할껀지)
newwall = list(combinations(nowall, 3))
total = 0
for i in newwall:
    bfs(i)

print(total)

