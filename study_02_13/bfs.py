# import sys
# sys.stdin = open("input.txt", "r")

# bfs
from collections import deque

N, M = map(int, input().split())

# 인접리스트 형태:인접된 것만 저장하는 형태
graph = [[] for _ in range(N+1)] #인덱스랑 숫자를 맞추기 위해

#간선 정보 입력
for _ in range(M):
    start, end = map(int, input().split())
    #인접 리스트 특징
    graph[start].append(end)
    #양방향 그래프(설정)
    graph[end].append(start)

def bfs(start): #파라미터가 리스트 형태
    #초기화
    dq =deque([start]) #리스트로 적어야 함
    visited = [0] *(N+1)
    visited[start] = 1
    print(start, end= ' ')
    while dq: #후보군이 비어있으면 끝
        now =dq.popleft()
        # visited[next_node] = 1 : 여기에 있어도 상관없음. 근데 메모리 효율이 별로. 중복된게 같이 들어가버림
        # print(now, end= ' ')

        for next_node in graph[now]:
            # 이미 방문한 노드면 pass
            if visited[next_node]:
                continue

            print(next_node, end= ' ')
            #방문 처리 먼저
            visited[next_node] = 1 # 이쪽이 더 효율적/ 후보군으로 등록하면서, 바로 방문처리(효율적)
            dq.append(next_node) #다음 후보군으로 등록하는 과정
            
bfs(1)

