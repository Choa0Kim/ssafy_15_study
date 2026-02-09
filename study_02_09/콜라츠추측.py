import sys
sys.stdin = open("input.txt", "r")
# 재귀호출 구조 :내 구조를 그대로 쓰는데, 데이터만 달라짐
# - 시작(현재시점):N
# - 끝: 1
# - 누적값(파라미터): 계산된 값
def recur(num):
    global cnt
    #num == 1 이라면 끝 
    if num == 1 :
        return 
    cnt += 1 #재귀호출 할 때마다 카운팅
    # num가 짝수면
    if num % 2 == 0:
        # 다음으로 넘겨주는데, 나누기 2해서
        recur(num // 2) 
    # num가 홀수면
    else:
        recur(num * 3 + 1)
        return 




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0  # cnt는 모든 재귀호출이 공유함. global로 만들기
    recur



    # N = 10
    
    # def recur(num):
    #     #종료 시점
    #     if num <= 1:
    #         return
    #     # 내 현재 시점은 10인데
    #     print(num, end=' ')
    #     # 다음으로 넘어갈 땐 5를 넘겨줌
    #     recur(num // 2)