# # 10진수를 2진수로 변환
# def decimal_to_binary(n):
#   binary_number = ""

#   if n == 0:
#     return "0"  # 0일때의 조건도 생각해야 함.

#   # 0보다 클 때까지 2로 나누면서
#   # 나머지를 정답에 추가
#   while n > 0 :

#     # 2로 나눈 나머지를 구해서
#     remain = n % 2
#     # 정답에 추가
#     binary_number = str(remain) + binary_number

#   # 2로 나누기
#     n = n // 2
#   return binary_number    

# print(decimal_to_binary(11))


# # 10진수를 16진수로 변환
# def decimal_to_hexadecimal(n):

#   # 딕셔너리, 문자열로 맵핑?
#   hex_digits = "0123456789ABCDEFG"
#   hexadecimal_number = ""

#   while n > 0:
#     remain = n % 16
#     hexadecimal_number = hex_digits[remain] + hexadecimal_number

#     n = n // 16

#   return hexadecimal_number  

# print(decimal_to_hexadecimal(16))

# # 내장 함수
# print(bin(5))
# print(hex(255))


# 비트 연산자

# 1. 1 << n -> 2^n을 구할 수 있다
# 부분집합 구하기
arr = [7, 1, 3, 5]

print(f"부분 집합의 수: {1 << len(arr)}개")

# 전체 부분 집합 구하기
# i = 부분집합 번호
for i in range(1 << len(arr)):
  print(f"{i}번 째 부분집합: ", end= ' ')
  subset = []
  # 각 자리수를 모두 확인
  for idx in range(len(arr)):
    if i & (1 << idx):
      subset.append(arr[idx])
      print(arr[idx], end= ' ')
  # if len(subset) == 2:    
  #   result.append(subset)    
  print()    

# 상태를 나타내는 플래그 (각 상태가 하나의 비트를 활용)
WALK = 1 << 1
ATTACK = 1 << 2
JUMP = 1 << 3

character_state = 0

# 상태 설정 함수
def set_state(state, flag):
  return state | flag







