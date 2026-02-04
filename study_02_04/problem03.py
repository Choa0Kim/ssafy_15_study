import sys
sys.stdin = open("input.txt", "r")

# # 좌표 상하좌우 순서의 델타리스트
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# y, x = 3, 1 #츨발점
# # 상하좌우 4방향
# for i in range(4):
#     now_y = y +dy[i]
#     now_x = x +dx[i]
#     print(now_y, now_x)
#
# #  대각선 포함 8방향
# dy = [-1, 1, 0, 1, 1, 1, 0, -1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
# y, x = 3, 1
#
# for i in range(8):
#     now_y = y + dy[i]
#     now_x = x + dx[i]
#     print(now_y, now_x)


# 1. 왼쩍, 위쪽이 없는 등 범위 밖을 처리해줘야 함.
# 2. 츨발지점이 여러 군데

T = int(input())
for test_case in range(1, T+1):

    # y, x = 0, 0 #츨발점
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    max_val = 0
    for i in range(N):
        for j in range(N):
            # (i, j) + i,j의 상하좌우 값 더하기
            total = arr[i][j]

            for k in range(4): # 4방향 탐색
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

# #------------- 강사님 풀이 ---------------
#
# # 상하좌우 델타
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# T = int(input())
# for test_case in range(1, T+1):
#
#     # y, x = 0, 0 #츨발점
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_y, max_x, max_total = 0, 0, 0
#
#     # sy, sx : 파리채를 치는 지점
#     for sy in range(N):
#         for sx in range(N):
#             #  (sy, sx) + 상하좌우 값 ->더하기기
#            total = arr[sy][sx]
#
#             for i in range(4):
#                 new_y = sy + dy[i]
#                 new_x = sx + dx[i]
#                 # 해당 방향의 좌표가 범위를 벗어나면 continue -델타 사용할 때는 같이 고려
#                 if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
#                     continue
#                 total += arr[new_y][new_x]
#             # 최대값 갱신
#             if total > max_total:
#                 max_y = sy
#                 max_x = sx
#                 max_total = total
#
#         print(f"#{tc} {max_total} {max_y} {max_x}")





