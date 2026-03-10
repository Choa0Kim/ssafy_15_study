from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board):
    q = deque(virus)

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))

    safe = 0
    for row in board:
        safe += row.count(0)

    return safe


ans = 0
E = len(empty)

for i in range(E):
    for j in range(i+1, E):
        for k in range(j+1, E):

            board = [row[:] for row in lab]

            x1, y1 = empty[i]
            x2, y2 = empty[j]
            x3, y3 = empty[k]

            board[x1][y1] = 1
            board[x2][y2] = 1
            board[x3][y3] = 1

            ans = max(ans, bfs(board))

print(ans)