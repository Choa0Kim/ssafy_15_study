import sys
sys.stdin = open("input.txt", "r")

# 입력 받을 빈 리스트
arr=[]
# 입력 받기
for _ in range(9):
  N = int(input())
  arr.append(N)

# print(arr)
#오름차순으로 출력해야 함. 먼저 sort
arr_sort = sorted(arr)
# print(arr_sort)

# 총 sum
total = sum(arr_sort)
# 범인 인덱스 저장 변수
idx1 = 0
idx2 = 0
flg = True
# 9명 중 1명 빼기
for i in range(0,9):
  total -= arr_sort[i]
  #해당 i번째 값 저장
  idx1 = arr_sort[i]
  # 8명중 1명 빼기
  for j in range(1,9): #앞에서 한 명을 뺏으니까 i는 1번부터
    total -= arr_sort[j]
    idx2 = arr_sort[j]

    if total == 100:
      #반복문 탈출: 조건으로 flg 변수 사용
      flg = False
      break
    # 100이 안나오면 다음 j+1번째를 확인하기 위해 total을 j번째를 빼기전으로 돌리기
    total += arr_sort[j]
  if flg == False:
    break
  # 다음 i+1번째를 확인하기 위해 total 값 초기화
  total += arr_sort[i]

# print(idx1, idx2)  

# 범인 인덱스 값을 찾았으면 범인 제외하고 출력
for i in range(len(arr_sort)):
  if arr_sort[i] != idx1 and arr_sort[i] != idx2:
    print(arr_sort[i]) 


  

  






