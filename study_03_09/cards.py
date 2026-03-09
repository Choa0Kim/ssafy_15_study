# 완전 탐색 문제 2. 연속 3장 트럼프카드
# 1. depth = 5
# 2. branch = 4
# 

# 2. 3장 연속된 카드를 갯수를 확인하는 함수
def count_three():
  if path[0] == path[1] == path[2] : return True
  if path[1] == path[2] == path[3] : return True
  if path[2] == path[3] == path[4] : return True
  return False


cards = ['A', 'J', 'Q', 'K']
# 근데 카드가 꼭 문자일 필요가 있나..?
# cards = [0, 1, 2, 3]
path = [] #경로 저장
result = 0
# 1. 전체 케이스 
# 카드 5장을 뽑는다(depth = 5)
# 한 번의 선택 -> 4개 중 하나(4가지의 경우의 수)

def recur(cnt):
  global result
  # 종료조건: 카드를 5장 뽑앗을 때
  # 카드 5장을 뽑는다(depth = 5)
  if cnt == 5:  # 5장을 골랐을때,
    print(path)
    # 만약 3장이 연속되면 result += 1 b
    # => 이런 식으로 조건이 있으면 함수로 빼기
    if count_three():
      print(*path)
      result +=1
    return 
  # 카드 4개 중 하나를 선택
  for i in range(4):
    path.append(cards[i])
    recur(cnt+1)
    path.pop()
  
  # # 0 선택
  # path.append(0)
  # recur(cnt +1)
  # # 0을 고르지 않은 상태로 1을 골라야함
  # # => 초기화
  # path.pop()
  # # 1 선택
  # path.append(0)
  # recur(cnt +1)
  # path.pop()
  # # 2 선택
  # path.append(0)
  # recur(cnt +1)
  # path.pop()
  # # 3 선택
  # path.append(0)
  # recur(cnt +1)
  # path.pop()
  
recur(0) 
print(result) 
