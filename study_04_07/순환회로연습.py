import sys
sys.stdin = open("input.txt", "r")



    
#루트 찾는 함수
# x 노드가 속한 집합의 루트를 찾는 함수
def find(x):
    #  자신이 루트이면 
    if x == parents[x]:
        return x #자기 자신을 리턴
    # 자신이 루트가 아니라면
    parents[x] = find(parents[x])
    return parents[x]

# 두 노드를 하나로 합치는 함수
# => 각 그룹의 루트끼리 합치는 
def union(y, x):
    rep_y = find(y)
    rep_x = find(x)
    # 만약 루트가 같으면 싸이클
    if rep_y == rep_x:
        return False
    # 루트가 다르다면 합치기 
    parents[rep_x] = rep_y #x의 루트를 y의 루트 밑으로
    return True 

def solution():
    for y in range(N):
        for x in range(y+1, N): #양방향이므로 인접행렬의 위에만 확인.
            #연결된 선이 아니라면
            if arr[y][x] == 0:
                continue #다음칸으로 넘어가기
                # 1인칸 발견 
                # => y노드와 x노드 사이에 선이 존재
            if union(y,x) is False : #  y노드와 x노드 사이에 사이클이 존재한다면 false
                return False
    # 사이클이 없다면 True
    return True
        

T = int(input())

for tc in range(1, 1+T):
    N = int(input()) #N: 노드 갯수
    # 인접행렬 
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 각 노드의 부모를 자기 자신으로 초기화 => 아직 연결된 상태가 아니기 때문에
    parents = [i for i in range(N)]
    # 예시1 기준 
    # 인덱스: 노드번호
    # 값: 부모 번호
    # parents = [0, 1, 2, 3, 4] 

    result = solution()
    if result:
        print(f'#{tc} STABLE')
    else:
        print(f'#{tc} WARNING')