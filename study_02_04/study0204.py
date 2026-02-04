# #3X4 배열- 0으로 채워진.
# arr = [[0]*4 for _ in range(3)]
# print(arr)


# # 배열순회(행 우선 순회)
# # n * m 개의 모든 원소를 순회
# for i in range(n): # 외부루프: 행 결정
#     for j in range(m): #내부루프: 열 결정
#         f(array[i][j])


# # 배열순회(열 우선 순회)
# # n * m 개의 모든 원소를 순회
# for j in range(m): # 외부루프: 행 결정
#     for i in range(n): #내부루프: 열 결정
#         f(array[i][j])

# # 역순순회(끝에서 거꾸로)
# for i in range(n-1, -1, -1):
#     for j in range(m-1, -1, -1):
#         f(array[i][j])

#  배열 크기와 저장된 값이 주어질 때 합 구하기(N X M)- 모든 원소의 합(행 우선)
# 입력 예시
# 3 4
# 1 7 2 8
# 6 2 9 3
# 5 7 4 2
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# s = 0
#
# for i in range(N):
#     for j in range(M):
#         s += arr[i][j]
# print(s)
#
# # 지그재그 순회
# # i 행의 좌표
# # j 열의 좌표
#
#
# for i in range(n):
#     for j on range(m):
#         f(array[i][j] + (m-1))

import sys
sys.stdin = open("input.txt", "r")
# 1. 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 2. 가로부터 접근 (인덱스)
for y in range(5):
    for x in range(5):
        print(arr[y][x], end = ' ')
    print()
print('--------------------------------')
# 세로부터 접근
for x in range(5):
    for y in range(5):
        print(arr[y][x], end = ' ')  # [앞]: 행을 이미
    print()
print('--------------------------------')
# 반복문은 고정하고, 내부 위치만 바꿔도 됨.
for i in range(5):
    for j in range(5):
        print(arr[j][i], end = ' ')
    print()
print('--------------------------------')

# 대각선 접근 - 반복 자체는 한 번 - for문 1개
# 우하단 대각선 (\) : (0,0) (1,1)....(4,4)
for i in range(5):
    print(i, i)
print('--------------------------------')
# 좌하단 대각선 (/) : (0,4), (1,3),(2,2),(3,1),(4,0) :y는 +1, x는 -1
for i in range(5): #y 좌표
    # print(i, 4-i)
    print(arr[i][4-i])
print('--------------------------------')
# 범위 접근
# - 3*3 사각형 범위값들을 한 번에 접금
#- 예시) 합이 가장 큰 범위 값을 구하기
sy, sx = 0,0  # 계산하고자 하는 출발지
total = 0
for y in range(sy, sy + 3): #출발지에서 출발지로부터 3칸
    for x in range(sx, sx + 3):
        total += arr[y][x]
print(total)

print('--------------------------------')
# 출발지가 0,0 -> 0,1로 되었을 때
sy, sx = 0,1 # 계산하고자 하는 출발지
total = 0
for y in range(sy, sy + 3): #출발지에서 출발지로부터 3칸
    for x in range(sx, sx + 3):
        total += arr[y][x]
print(total)
print('--------------------------------')

# 출발지가 0,0 -> 0,3로 되었을 때 => 에러남(0,5가 없음)범위 밖
sy, sx = 0, 3 # 계산하고자 하는 출발지
total = 0
for y in range(sy, sy + 3): #출발지에서 출발지로부터 3칸
    for x in range(sx, sx + 3):
        #[범위 밖 계산 체크를 항상 해냐야 함
        # 1.범위 밖으로 넘어았을 때는 계산 X [권장]
        #  조건에 따라 계산할 수 있어서, 가독성이 좋음(and말고 or), continue 사용)
        if y > 4 or y < 0 or x > 4 or x < 0:
            continue
        total += arr[y][x]
print(total)
print('--------------------------------')


# 2. 범위안에 들어왔을때만 계산
#  추후 가독성이 떨어짐
sy, sx = 0, 3 # 계산하고자 하는 출발지
total = 0
for y in range(sy, sy + 3): #출발지에서 출발지로부터 3칸
    for x in range(sx, sx + 3):
        #[범위 밖 계산 체크를 항상 해냐야 함
        # 1.범위 밖으로 넘어았을 때는 계산 X
        if 0 <= y <= 4 and 0 <= x <= 4:
            total += arr[y][x]
print(total)
print('--------------------------------')

# 시작점 좌표 수정(위는 고정 되어 있음
# max_total = 0
# max_y, max_x = 0, 0
# for sy in range(5):
#     for sx in range(5):
#     # 3X3 범위 계산 시작
#         total = 0  # 계산을 할 때마다 0으로 리셋되어야 함.
#         if y > 4 or y < 0 or x > 4 or x < 0:
#             continue
#         max_total += arr[y][x]
#         # max_total = max(max_total, total) #값만 필요하다면
#     # 좌표값까지 같이 저장
#         if total > max_total:
#             max_y = sy
#             max_x = sx
#
# print(max_y, max_x, max_total)


print('--------------------------------')
# 출발지를 전달받아서, 3*3 영역의 합을 계산하는 함수
def cal_total(sy, sx):
    total = 0
    for y in range(sy, sy + 3):  # 출발지 ~ 출발지 + 3
        for x in range(sx, sx + 3):
            # 범위 밖 계산 체크를 항상 합시다!
            # 1. [권장] 범위 밖은 계산하지 마라
            if y > 4 or y < 0 or x > 4 or x < 0:
                continue

            total += arr[y][x]

            # 2. 범위 안에 들어왔을 때만 계산해라
            #   - 추후 조건이 많아지면 가독성이 떨어진다.
            # if 0 <= y <= 4 and 0 <= x <= 4:
            #     total += arr[y][x]

    return total



max_total = 0
max_y, max_x = 0, 0

# 계산하고자 하는 출발지를 반복
for sy in range(5):
    for sx in range(5):
        total = cal_total(sy, sx)
        # max_total = max(max_total, total)  # 값만 필요하다면
        # 좌표값까지 같이 저장
        if total > max_total:
            max_total = total
            max_y = sy
            max_x = sx

print(max_y, max_x, max_total)

# ------------- 강사님 풀이 ---------------

# 상하좌우 델타

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(input())
for test_case in range(1, T + 1):

    # y, x = 0, 0 #츨발점
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_y, max_x, max_total = 0, 0, 0

    # sy, sx : 파리채를 치는 지점
    for sy in range(N):
        for sx in range(N):
            #  (sy, sx) + 상하좌우 값 ->더하기기
            total = arr[sy][sx]

            for i in range(4):
                new_y = sy + dy[i]
                new_x = sx + dx[i]
                # 해당 방향의 좌표가 범위를 벗어나면 continue -델타 사용할 때는 같이 고려
                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                    continue
                total += arr[new_y][new_x]
            # 최대값 갱신
            if total > max_total:
                max_y = sy
                max_x = sx
                max_total = total

    print(f"#{tc} {max_total} {max_y} {max_x}")







