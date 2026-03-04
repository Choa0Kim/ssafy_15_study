import sys
sys.stdin = open("input.txt", "r")
# float 이진수 변환
# bin, format은 int 전용
# 주어진 소수에 *2를 해서 정수부분을 기록하고, 소수부분 넘기기, 
# 넘겨진 소수부분에 다시 *2 
# 소수부분이 0일 될때 까지 반복

T = int(input())
for tc in range(1, 1+T):
  N = float(input())
  # 정구부분 담을 빈 문자열
  result = ""
  while N > 0 :
    N *= 2
    intt = int(N)
    # 문자열에 넣기위해 str 변환
    result += str(intt)
    # 소수부분만 남기기
    N -= intt
  if len(result) > 12:
    print(f'#{tc} overflow')
  
  else:
    print(f'#{tc} {result}')

    



  
  
