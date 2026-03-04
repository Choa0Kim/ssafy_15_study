import sys 
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, 1+T):
  # 글자수랑 문자열따로 받기
  N, strr = input().split()
# 변환된 이진수들을 담을빈 str만들기   
  result = ""
  # 문자열을 한글자씩 떼기
  for s in strr:
    #한 글자씩 10진수로 변환
    decimal_val = int(s, 16)
    # 10진수로 변환한 것을 2진수로 변환
    # '04b': 1.0 채움문자, 2. 최소너비(결과 문자열을 최소 4글자로 맞춰라) 3.b:이진변환
    binary_val = format(decimal_val, '04b')
    # 결과를 문자열에 넣기
    result += binary_val
print(f'#{tc} {result}')
  
#   # 각 자리수에 16의 거듭제곱을 곱해서 10진수로 
#   # 문자열과 숫자열이 합쳐있기 때문에 10진수로 먼저 바꾸고 다음에 2진수로 변환
#   # 결과에 0b가 따라옴.
#   # 슬라이싱으로 제거가능
#   # binary_val = bin(decimal_val)[2:]  

