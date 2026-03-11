import sys
sys.stdin = open("input.txt", "r")

# 숫자가 존재하고, 숫자의 정수값을 찾기

# 1.mid 값을 본다
# 2. mid * mid 이 target보다 작다 -> 오른쪽을 탐색
#    mid * mid 이 target보다 크다 -> 왼쪽을 탐색


# 각 단계에서 mid와 target을 가지고 조건을 검사
# - 조건이 True 일 때 오른쪽을 탐색
def check(mid, target):
  if mid * mid <= target:
    return True
  return False


def binary_search(target):
  left, right = 0, target
 
  while left <= right:
    mid = (left+right) // 2

    # mid * mid 이 target보다 작다 -> 오른쪽을 탐색
    if check(mid, target): # 조건을 함수로 빼줌 => parametric search
      left = mid +1
    else:
      right = mid -1

  # left: 조건을 처음으로 만족하지 않는 값 
  # right: 조건을 만족하는 마지막 값

  # left는 정답의 바로 우측에 정지
  # => 1을 빼준 값을 return
  return left -1


  
T = int(input())

for tc in range(1, 1+T):
  target = int(input())


  result = binary_search(target)
  print(f'#{tc} {result}')
  
  