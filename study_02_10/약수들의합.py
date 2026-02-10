#시작값: 1
# 끝점: n//2\
# num: 1씩 증가하는 숫자, acc_list: 약수리스트

import sys
sys.setrecursionlimit(10**6)

def recur(num, acc_list): #acc_list 초기값 설정?X >빈 리스트인 인자로받기
    # 종료조건
    if num > N // 2:
        return acc_list
    #약수체크
    if N % num == 0: 
        acc_list.append(num)
    
    return recur(num + 1, acc_list) 

while True:
    N = int(input())

    if N == -1:
        break
    divisors = recur(1, [])
    #완전수인 경우
    if sum(divisors) == N:
        print(f'{N} = {"+".join(map(str, divisors))}')
    #완전수가 아닌 경우    
    else:
        print(f'{N} is NOT perfect.')   



