import sys 
sys.stdin = open("input3.txt", "r")

# T = int(input())
# for tc in (1, 1+T):
# code = ""  
N, M = map(int, input().split())
# 중복이 없는 줄 담는 딕셔너리
unique_code = set()
# 0만 있는 행 무시하기
for _ in range(N):
  strr = input().strip()
  # 양 옆에서 0을 지웠을때, 빈문자열이 있는지 확인 => 유효한 암호가 있는 줄  
  if strr.strip('0'):
    # 그 줄은 딕셔너리에 담기
    unique_code.add(strr)

# 딕셔너리를 리스트로 바꾸기
unique_list = list(unique_code)

# unique_code에 들어있는 줄을 2진수로 변환
for hex_row in unique_list:
  binary_row = ""
  for char in hex_row:
    binary_row += format(int(char, 16), '04b')

# binary_list = list(binary_row)
# print(binary_list)


# 암호 비율 딕셔너리
ratio_map = {
    (3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4, (1, 2, 3, 1): 5, (1, 1, 1, 4): 6, (3, 1, 2): 7,
    (2, 1, 3): 8, (3, 1, 1, 2): 9
}
# c1:c2:c3:c4
i = len(binary_row) -1
while i >= 55:
  if binary_row[i] == '1':
    # 8개 코드 담는 리스트
    code_list = []

    # 3개의 비율만 고려하는 이유
    # c1 앞에 무의미한 0이 까려 있음. while문으로 갯수를 세면. 무의미한 0까지 세어짐.
    #
    for _ in range(8):
      c2 = c3 = c4 = 0
      # (c4=> 1갯수세기)
      while binary_row[i] == '1': c4 += 1; i -= 1
      # (c3=> 0 갯수세기)
      while binary_row[i] == '0' : c3 += 1; i -= 1
      # (c2=> 0 갯수세기)
      while binary_row[i] == '1' : c2 += 1; i -= 1


      # 갯수 센 것들 비율 확인
      K = min(c2, c3, c4)

      # c1 계산
      c1 = (7*K)- (c2+c3+c4)
      # c1:c2:c3:c4 비율 맞추기
      a = (c1//K, c2//K, c3//K, c4//K)
      b = ratio_map[a]
      code_list.append(b)
      print(code_list)

      i -= c1

      # for k in range(0, 56, 7):
        
      
      


      


      
      
    
    result = binary_row[i-55:i+1]

  else:
    i -= 1

print(result)

    
# print(binary_row)

# # 뒤에서 부터 확인하면서 1로 시작하는지 확인.
# for i in range(M-1, -1, -1):
#   if 











# 1. 0만 있는 행은 무시한다
# 2. 같은 행이 여러 번 나오면 하나만 사용한다
# 3. 16진수 데이터를 2진수로 변환한다
# 4. 왼쪽의 의미 없는 0은 제거한다
# 5. 바코드는 항상 1로 끝나므로 오른쪽부터 스캔한다
# 6. 숫자는 1-0-1 패턴으로 구성된다. (각각이 구간)
# 7. 세 구간 길이를 최소값으로 나누어 비율을 구한다
# 8. 비율을 이용해 숫자를 해독한다
# 9. 숫자 8개가 모이면 하나의 암호가 완성된다
# 10. 검증 코드 공식으로 올바른 암호인지 확인한다
# 11. 이미 나온 암호라면 중복 계산하지 않는다
