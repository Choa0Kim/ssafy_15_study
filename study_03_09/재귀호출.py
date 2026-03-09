# 재귀함수: 자기자신을 호출하는 함수
# 1. 시작
# 2. 끝
# 3. 누적된 값

#0~ 10을 출력
# - 0부터 시작
#- 10에사 종료(10보다 커지면 종료)


# def recur(num):
#   if num > 3:
#     return
  
#   print(num, end=' ')  
#   recur(num+1)
#   recur(num+1)

# recur(0)

# # 0 1 2 3 3

# def recur2(num):
#   if num > 3:
#     return 
  
#   for i in range(1, 7):
#     recur2(num+1)

# 중복 순열
# [0, 1, 2] 3개의 카드가 존재(2개를 뽑는 모든 경우)

# 기저조건: 2개의 카드를 모두 뽑았을 경우
# 시작: 0개의 카드를 고른 상태부터 시작
# 다음 재귀 호출: 카드 3개 중 하나를 선택
# path = []
# def recur(cnt):
#   if cnt == 2:
#     print(path)
#     return

#   #1. 넘길 조건 선택
#   # 0을 선택 (카드뽑기)
#   path.append(0)
#   recur(cnt+1)
#   # 마지막에 뽑은 카드를 리셋
#   path.pop()
#   # 1을 선택
#   path.append(1)
#   recur(cnt+1)
#   # 마지막에 뽑은 카드를 리셋
#   path.pop()
#   # 2를 선택
#   path.append(2)
#   recur(cnt+1)
#   # 마지막에 뽑은 카드를 리셋
#   path.pop() 


# recur(0)

# 위 코드를 반복문으로
path = []
def recur(cnt):
  if cnt == 2:
    print(path)
    return
  # 한 번의 선택에서 3가지 경우의 수
  for i in range(3):
    # 주의. in은 O(N)이라서 느림=> 시간초과 가능성 높음
    if i in path: # 이미 뽑은 숫자라면 다음 숫자를 고려하자
      continue
    path.append(i)   # 해당 숫자를 경로에 추가
    recur(cnt+1)
    path.pop()   # 숫자를 뽑은 적이 없도록 초기화



# 심화. 경로를 전역변수 쓰지 않고 하는 방법


# # 중복 없애기
# path = []
# N = 3
# used = [0] * N  #N개의 종류가 있을 경우 N개 만큼 만듦   

# def recur2(cnt):
#   if cnt ==3:
#     print(*path)
#     return
  
#   for i in range(3):
#     if used[i]:  # 이미 i를 사용한 적이 있다면
#       continue
#     used[i] =1 #방문처리
#     path.append(i)
#     recur2(cnt+1)
#     path.pop()
#     used[i] = 0 # 방문기록 초기화

# recur2(0)



