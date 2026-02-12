n = int(input())

# 재귀함수
def recur(n, ans=""):

    # 탈출조건
    # 입력값이 1 또는 0일때 문자 1 반환
    if n <= 1:
        return "1"
    
    # 재귀로직
    # 짝수일때(2로 나눴을 때, 나머지가 0)
    if (n%2== 0):
        ans = recur(n//2, ans) + "0"
        return ans
    
    # 홀수일떄
    else: 
        ans = recur(n//2, ans) + "1"
        return ans
    
# 함수실행
print(recur(n))