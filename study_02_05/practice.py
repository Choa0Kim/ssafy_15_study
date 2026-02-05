# 딜팽이 슷자
# 우하좌상 순서
# 1. 갈 수 있으면 끝까지 이동
# 2. 막히면 방향 전환

# 1. 현재 숫자(current)가 1부터 N^2까지 반복
# 2. 방향배열: 우하좌상 순서
# 3. 바라보고 있는 방향 -> 계속 전진
#   - 방향 회전
#       - 벽을 만나거니
#       - 이미 숫자가 있는 곳을 만나면

# T = int(input())
# dy = [0, 1, 0 ,-1]
# dx = [1, 0, -1, 0]

# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = [[0]* N for _ in range(N)]
# y, x = 0, 0
# current = 1
# direction = 0

# while current <= N * N:
#     arr[y][x] = current #현재 자리에 숫자 저장

#     ny = y + dy[direction]
#     nx = x + dx[direction]
#     # if 다음 좌표가 범위 밖 or 이미 데이터가 있다면:
#     # 방향전환
#     if ny < 0 or ny >= N or nx < 0 or nx >= N or arr[nx][ny] != 0:

#         current += 1 # 다음 숫자
#------------------------------------------------------------

# 슬라이싱 윈도우
# - 창(범위)이 미끄러지면서 범위에 대한 계산을 하는 문제들에서 
#   해당 범위값을 반복문이 아니라 
#   제외되는 부분을 없애주고
#   추가되는 부분만 계산해주는 방식


# 연속된 k 개의 숫자의 합 중 가장 큰 합을 구하기
arr = [20, 32, 16, 25, 36, 23, 42, 53, 63, 46]

k =5
window = sum(arr[:k])
max_sum = window # 첫 윈도우값 초기화

# window = window - arr[0] + arr[3]
# print(window)

# window = window - arr[1] + arr[4]
# print(window)

# window = window - arr[i] + arr[k + i]
for i in range(len(arr)-k):
    window = window - arr[i] + arr[k+i]
    print(f'{i}위치합 = {window}')
    if window > max_sum:
        max_sum = window
print('최대 합:', max_sum)        
