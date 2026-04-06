# swea 순환회로 검사
# 1. 각 노드를 하나의 집합을 보기
# 2. 하나씩 연결 
    # - 다른 집합이면 연결 ok
    # - 같은 집합이면 연결 => Warning(사이클 발생)
import sys
sys.stdin = open("input.txt", "r")

def find(x):
    if x == parents[x]: # 본인이 대표자
        return x
    parents[x] = find(parents[x]) # 부모가 대표자인지 확인
    return parents[x]

def union(y, x):
    rep_y = find(y)
    rep_x = find(x)

    #대표자가 같다 -> 같은 집합끼리 연결하려는 시도
    if rep_y == rep_x:
        return False   
    parents[rep_x] = rep_y
    return True

def solution():
    for y in range(N):
        for x in range(y + 1, N):
            if arr[y][x] == 0 :
                continue

            # y, x를 연결
            # 만약 같은 집합끼리 union 하려고 하면 False가 반환
            # -> 사이클 발생!
            if union(y, x) is False:
                return False
    return True
        
T = int(input())

for tc in range(1, T+1):

    # 인접 행렬..?
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(graph)
    
    parents = [i for i in range(N)] # make_set

    # 우상단 삼각형을 반복해서 확인
    #(y, x) 좌표가 1이라면 연결
    #   - 다른 집합이면 같은 집합으로 병합
    #   - 같은 집합끼리 연결 => 싸이클 발생(WARNING 출력)하고 끝
    result = solution()
    if result:
        print(f'#{tc} STABLE')
    else:    
        print(f'#{tc} WARNING')


    



    