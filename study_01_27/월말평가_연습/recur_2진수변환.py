
# 표준 입력
n = int(input())

# 재귀함수
def func(n, ans=""):

    # 탈출 조건
    # 입력값이 1, 또는 그 이하일때, 문자 1을 반환
    if n <= 1:
        return "1"

    # 재귀 로직
    # 짝수일때,
    if(n%2 == 0):
        # 기존 문자에서 0을 추가
        ans = func(n//2, ans) + "0"
        return ans
    
    # 홀수일때,
    else:
        # 기존 문자에서 1을 추가
        ans = func(n//2, ans) + "1"
        return ans

# 함수 실행
print(func(n))
