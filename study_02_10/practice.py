# 재귀호출
# - 특정 상황에 중간에 끊자! -> 백트래킹
# - 재계산 하지말자! -> 메모이제이션
# - 그래프의 완전탐색에 활용하자! -> DFS

def fibo(num):
    #종료조건: num이 0 or 인 경우
    #=> 0번째, -1번째는 없음
    if num <= 1:
        return num
    # 만약 memo에 num이라는 key가 있다면
    if memo.get(num):
        return memo[num]
    # 아니라면 계산한 값을 memo에 넣고
    memo[num] = fibo(num-1) + fibo(num-2)
    return memo[num]  #해당 키(num)의 value를 리턴


N = int(input())
# memo 이미 계산한 값을 저장.
memo = {}
result=fibo(N)
print(result)
