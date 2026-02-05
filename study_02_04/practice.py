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

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0

for i in range(N):
    for j in range(M):
        s += arr[i][j]
print(s)

# 지그재그 순회
# i 행의 좌표
# j 열의 좌표


for i in range(n):
    for j on range(m):
        f(array[i][j] + (m-1))
    


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



sy, sx = 0, 3 # 계산하고자 하는 출발지
total = 0
for y in range(sy, sy + 3): #출발지에서 출발지로부터 3칸
    for x in range(sx, sx + 3):
        #[범위 밖 계산 체크를 항상 해냐야 함
        # 1.범위 밖으로 넘어았을 때는 계산 X
        if 0 <= y <= 4 and 0 <= x <= 4:
            total += arr[y][x]
print(total)





