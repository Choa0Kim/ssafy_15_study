import sys
sys.stdin = open("input.txt", "r")

# baby-gin
# depth: 3 branch: 6?


#1. 전체 순열을 만들기 -  6개의 카드로 모든 순열: 전체 케이스
# + 중복 불가
path = []  #경로저장
used = [0] * 6 #카드 사용 유무
result = False # 전체 결과

# 1. 전체 순열을 먼저 구현
# - 종료조건: 6개의 카드를 모두 줄 세우면 종료 (depth=6)
# - 재귀호츨: 6개의 카드 (branch = 6)
# - 중복을 제가 해줘야 함.(고르는 수에)
# baby-gin 검사
def is_baby_gin():
  cnt = 0
  # 앞의 3개 숫자가 
  # run + triplet 비교 
  a, b, c = path[0], path[1], path[2]
  if a== b== c : # triplet
    cnt +=1
  elif a == (b-1) == (c-2): # run
    cnt +=1
  # 뒤의 3개 숫자가
  # run + triplet 비교 
  a, b, c = path[3], path[4], path[5]
  if a== b== c : # triplet
    cnt +=1
  elif a == (b-1) == (c-2): # run
    cnt +=1


  return cnt == 2

def recur(cnt):
  global result 
  # 종료조건
  if cnt == 6:
    # print(*path)
    if is_baby_gin():
      result = True
    return
  #재귀호출 조건
  for i in range(6):
    if used[i]:
      continue
    used[i]= 1 # 사용체크
    path.append(cards[i])
    recur(cnt+1)
    path.pop()
    used[i] = 0 # 초기화

cards = list(map(int, input().split())) 
recur(0)

print(result)











