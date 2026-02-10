#N 범위 좁음. - 재귀
# N = N

# 시작점 :N
# 끝점: 1
# 누적값: n -> 1 내려가는 숫자


def factorial(num):
    if num <= 1: # ==(x), 0!는 =1 , 0도 가능
        return 1
    
    return num * factorial(num-1)   #n x (n-1)!


N = int(input())
result = factorial(N)


