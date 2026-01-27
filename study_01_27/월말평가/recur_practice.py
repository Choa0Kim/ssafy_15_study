N = int(input())

def recur(N, ans=""):
    
    # if에 탈출조건 설정
    # 입력 값이 1, 또는 그 이하일 떄, 문자 1을 반환

    if N <= 1:
        return "1"  
    
    # 재귀 로직
    # 짝수일때
    if(N % 2 == 0):
        # 기존 문자에서 0을 추가
        ans = recur(N//2, ans) + "0"
        return ans
    
    # 홀수일때
    else: 
        # 기존 문자에서 1을 추가
        ans = recur(N//2, ans) + "1"
        return ans
    
print(recur(N))
