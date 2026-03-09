# 4개의 카드 중 5장을 뽑은 것 중에서  3장의 연속된 카드를 가지고 있는 경우의 수 


# 
cards = ['A', 'J', 'Q', 'K']

# 경로 저장
path = []


# 최종 경우의 수(조건에 맞는)
result = 0
# 1. 전체 케이스 확인
# 5장을 카드를 뽑음: depth = 5
# 4장의 카드 중에서(4개의 선택지): branch = 4
def recur(cnt): # cnt: 카드를 뽑은 갯수

  # 종료조건: 5장을 뽑았을 때
  if cnt == 5 :
    # 종료시점에 반환할 결과물: 조건에 맞는 최종 경우의 수 (result)
    print(path)
  # 재귀조건: 카드를 한 장씩 뽑을때
  # 'A'를 뽑은 경우
  path.append(cards[0])
  # 뽑고 다음 카드를 뽑기 위해 재귀 호출
  # 카드를 한 장 뽑았으니 cnt+1 해줘서 넘기기
  recur(cnt +1)
  path.pop() 
  
  # 'J'를 뽑은 경우
  path.append(cards[1])
   # 뽑고 다음 카드를 뽑기 위해 재귀 호출
  # 카드를 한 장 뽑았으니 cnt+1 해줘서 넘기기
  recur(cnt+1)
  path.pop() 

  # 'Q'를 뽑은 경우
  path.append(cards[2])
   # 뽑고 다음 카드를 뽑기 위해 재귀 호출
  # 카드를 한 장 뽑았으니 cnt+1 해줘서 넘기기
  recur(cnt+1)
  path.pop() 

  # 'K'를 뽑은 경우
  path.append(cards[3])
   # 뽑고 다음 카드를 뽑기 위해 재귀 호출
  # 카드를 한 장 뽑았으니 cnt+1 해줘서 넘기기
  recur(cnt+1)
  path.pop() 


recur(0)




  




  # 