import sys 
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# print(numbers)
total = 0
# 첫번째 카드 설정
for i in range(N):
  total += numbers[i]
  card1= numbers[i]
  # 두번째 카드 설정
  for j in range(1, N):
    total += numbers[j]
    card2 = numbers[j]
    # 세번째 카드 설정
    for k in range(2, N):
      total += numbers[k]
      card3 = numbers[k]

      # total의 값을 M과 비교
      if total <
      
