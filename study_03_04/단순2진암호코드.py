# 힌트: 암호코드의 끝부분(배열 오른쪽)부터 탐색

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, 1+T):
  N, M = map(int, input().split())
  # print(N, M)

  # 0제외.v1 문자열
  # 암호 부분만 빼기
  # 한 줄씩 읽기
  # result = []
  for i in range(N):
    num = input()
    # 줄에 1이 인다면
    if '1' in num :
      # 그 줄의 가장 오른쪽의 1 위치를 찾기
      for j in range(M-1, -1, -1):
        # 위치를 찾았다면
        if num[j] == '1':
          result = num[j-55:j+1]
          break  

  # re_result = reversed(result)
  # # 리스트말고 알맹이만 가져오가
  # re_result = "".join(reversed(result))
  # print(re_result)

  # 암호 코드 딕셔너리 만들기 => 암호는 키로하고 값은 value로 하는게 편함......
  code_dict = {
    0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001',
    6: '0101111', 7: '0111011', 8: '0110111', 9: '0001011'
  }  

  # key , value 바꾸기...
  re_code_dict = {v: k for k, v in code_dict.items()}

  # 숫자 암호로 바꾸기
  code_list = []
  for k in range(0, 56, 7):
    a = result[k:k+7]
    b = re_code_dict[a]
    code_list.append(b)

  # print(code_list)  
  # 유효암호 확인
  # 짝수만 찾기
  c = sum(code_list[0:7:2])*3
  # 홀수만 찾기
  b = sum(code_list[1:7:2])
  # 마지막 번호
  d = code_list[-1]
  # 총합
  total = c+b+d

  # print(total)
  if (total) % 10 == 0:
    print(f'#{tc} {sum(code_list)}')
  else:
    print(f'#{tc} 0')



