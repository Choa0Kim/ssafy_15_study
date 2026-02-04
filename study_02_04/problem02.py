import sys
sys.stdin = open("input.txt", "r")
# 델타
# 변화량을 리스트에 담아두는 것
'''
1. delta list 구현
2. delta 값을 누적해나가면서 계산

4
10 20 30 40
2
0 3 5
1 3 -10

delta: 5 -10 0 0
now_delta : -5
'''

T = int(input())

for tc in range(1, T +1):
    N = int(input())
    arr = list(map(int, input().split()))
    delta = [0] * (N+1) #델타 배열 만들기. 마지막 인덱스는 버림
    P = int(input())
    for _ in range(P):
        start, end, cost = map(int, input().split())
        delta[start] += cost
        delta[end + 1] -= cost

    current_delta = 0
    for i in range(N):
        current_delta += delta[i] #누적
        arr[i] += current_delta
    print(f'#{tc}',*arr)
print(request)
# [참고] f-string 안에 넣고싶다면 아래와 같이 join 활용
print(f'#{tc} {" ".join(map(str, arr))}')

# #  대각선 포함 8방향
# dy = [-1, 1, 0, 1, 1, 1, 0, -1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
# # y, x = 3, 1
#
# for i in range(8):
#     now_y = y + dy[i]
#     now_x = x + dx[i]
#     print(now_y, now_x)

di = [-1, 1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for test_case in range(1, T+1):
    # y, x = 0, 0 #츨발점
    # N = len(arr)
    arr = [list(map(int, input().split())) for _ in range(100)]
    N = len(arr)
    max_val, now_i, now_j = 0, 0, 0
    for i in range(N):
        for j in range(N):
            # (i, j) + i,j의 상하좌우 값 더하기
            total = arr[i][j]

            for k in range(8): # 4방향 탐색
                # total =0 # 한 턴 돌때마다 리셋
                # nj, ni: 이동한 후 새로운 열, 행 좌표
                # i: 현재 행
                # di[k]: 방향에 따른 변화량
                nj = j + dj[k] # 현재열 + 반향에 따른 변화량 더하기
                ni = i + di[k] # k=4 : 4방향의 값 다 더해짐
                # total += arr[ni][nj]
                # 해당 좌표가 범위를 벗어나는지 확인
                if 0 <= ni < N and 0 <= nj < N:
                    total += arr[ni][nj]
            # total += arr[i-1][j], arr[i+1][j], arr[i][j-1], arr[i][j+1]
            if total > max_val:
                max_val = total
                now_i = i
                now_j = j

    print(f'#{test_case}', max_val, now_i, now_j)

