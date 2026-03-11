import sys
sys.stdin = open("input.txt", "r")

# 완탐 불가
# 1. target= 자르는 길이
# 2. 해당 길이로 k개를 만들 수 있는지 확인

# mid 길이로 K개를 자를 수 있는가?
def check(mid):
   cnt = 0

   for c in chu:
      cnt += c // mid

      if cnt >= K :  #K개 이상 츄러스를 만들 수 있다
        return True
      
   return False

   
# 구하고자 하는 targey - 츄러스의 길이
# -left, right, mid가 츄러스의  길이를 의미한다는 뜻
#  -> mid 의 길이로 K개를 만들 수 있는가?
#   - K개 이상 자를 수 있다면 더 긴 길이 탐색
#   - K개를 못 만든다면 더 짧은 길이를 탐색

def binary_search():
  # 검색할 범위 지정(N)에서
  left, right = 1, max(chu) # 츄러스의 가장 짧은 것부터 긴 것까지 범위
  # 탐색 범위가 남아있는 동안 계속 반복
  while left <= right :
    # 중간지점 인덱스 계산
    mid = (left + right) // 2   
    # 있다면 더 긴 길이를 탐색
    if check(mid):
        left = mid + 1
    # 없다면 짧은 길이를 탐색
    else:
       right = mid - 1 
  return left - 1

T = int(input())

for tc in range(1, 1+T):
  N, K = map(int, input().split())
  chu = [int(input()) for _ in range(N)]
  result = binary_search()
  print(f'#{tc} {result}')






  # for _ in range(N):
  #   c = int(input())
  #   chu.append(c)
  # print(chu)