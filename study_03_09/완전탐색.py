# 완전 탐색
# 모든 가능한 경우의 수를 다 탐색

# 주사위 3개를 던져서 합이 10이하인 케이스의 수
# 상태 공간 트리
# - 주사위 3개 -> depth:3
# - branch 수: 1~6 숫자 ->6

# result = 0
# path = []

# def recur(cnt):
#   global result
#   if cnt == 3:
#     if sum(path) <= 10: # 경로의 합이 10 이하라면
#       print(*path)
#       result += 1
#     return
  
#   for num in range(1, 7):
#     path.append(num)
#     recur(cnt +1)
#     path.pop()


# recur(0)
# print(result)   


# 위 코드 효율적으로
# 1. 이미 10을 넘은 경우.=>가지치기
# 2. append말고 누적값을 파라미터로=> 내 경로에서 어떤 파라미터가 필요한지 

# result = 0
# path = []

# def recur(cnt, total):
#   global result
#   # 이미 10을 넘었으면, 이 케이스는 더 볼 필요없음
#   # 벡트레킹 원리
#   if total > 10:
#     return
#   if cnt == 3:
#     # 경로의 합이 10이하 라면
#     if total <= 10:
#       result += 1
#     return
  
#   for num in range(1, 7):
#     recur(cnt+1, total + num)

# recur(0, 0)







