# 

def fibo(num):
    if num <= 1:
        return num
    # 계산한 적 있으면
    if memo.get(num):
        return memo[num] #기존 기록된 값을 return
    #기록 코드
    memo[num] = fibo(num-1) + fibo(num-2)
    return memo[num] #한 번이라도 이 연산을 진행하면 위의 코드로 인해 딕셔너리로 저장

N = int(input())
#한 번이라도 연산된 것은 딕셔너리로 들어감
memo = {}
result = fibo(N)
print(result)