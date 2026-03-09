# 4개의 카드 중 5장을 뽑은 것 중에서  3장의 연속된 카드를 가지고 있는 경우의 수 




# 연속된 카드 확인 함수
def check():
  if path[0] == path[1] == path[2]: return True
  if path[1] == path[2] == path[3]: return True
  if path[2] == path[3] == path[4]: return True
  # 중복이 없다면 False반환: False는 result에 경우의 수를 추가하지 않음.
  return False
# 최종 경우의 수(조건에 맞는)
# 종료시점에 반환할 결과물: 조건에 맞는 최종 경우의 수 (result)

# 
cards = ['A', 'J', 'Q', 'K']

# 경로 저장
path = []
result = 0
# 1. 전체 케이스 확인
# 5장을 카드를 뽑음: depth = 5
# 4장의 카드 중에서(4개의 선택지): branch = 4
def recur(cnt): # cnt: 카드를 뽑은 갯수

  global result
  # 종료조건: 5장을 뽑았을 때
  if cnt == 5 :
    print(path)
  # 결과물인 path에 3장의 연속된 카드가 있는지 확인
    # 연속카드 확인 함수 호츨
    if check(): # check 함수가 True라면
     print(*path)
     result += 1
     
    return result

  # 재귀조건
  for i in range(4):  #cards 갯수
    # cards에 첫번째 카드 뽑고
    path.append(cards[i])
    # 다음 카드 뽑기위해 재귀 호출
    recur(cnt+1)
    # 종료조건 만나면 다음 카드 뽑기 위해. 마지막 카드 빼기 
    path.pop()



recur(0)
print(result)



