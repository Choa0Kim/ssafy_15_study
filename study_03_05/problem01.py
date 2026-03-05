# 2진수 7자리 받는 함수
def func(binary_str):
  number = ""

  # 전달빋은 문자열을 뒤에서부터 탐색
  for n in range(-1, len(binary_str)-1, -1):
    # 10진수로 변환하면서 계산
    while n > 0:
      remain = n % 10

      number = str(remain) + number
      n = n //2

    
    return number 
   

# 문자열 입력
word = input().strip()

for i in range(0, len(word), 7):
  result = func(word[i:i+7])
  print(result)

