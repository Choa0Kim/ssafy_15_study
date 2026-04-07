import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    # print(N,M, li)
     
    # 조 편성전 
    parents = [i for i in range(N+1)] 
    
    # 루트 찾는 함수
    def find(x):
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    
    def union(y, x):
        rep_y = find(y)
        rep_x = find(x)

        if rep_y != rep_x:
                parents[rep_x] = rep_y

    # 입력받은 리스트대로 실제 조 짜기
    for i in range(0, len(li), 2): #2명씩
        union(li[i], li[i+1])

    # 조 갯수 세기
    ans = 0
    for i in range(1, N+1):
        if parents[i] == i:
            ans += 1

    print(f'#{tc} {ans}')
            
    
    


    
