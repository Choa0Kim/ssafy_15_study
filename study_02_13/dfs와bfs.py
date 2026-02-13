import sys
sys.stdin = open("input.txt", "r")

result= []
#dfs 함수
def dfs(node):
    #최종 task: 현재의 방문한 노드 출력
    result.append(node)
    #1번 노드부터 N번 노드까지 순회
    for next_node in range(1, N+1):
        if graph[node][next_node] == 0:
            continue
        if visited[next_node] == 1:
            continue
        # 둘 다 해당 안되면
        visited[next_node] = 1 # 방문처리
        # 함수에 현재 노드 전달
        dfs(next_node)


N, M, V = map(int, input().split())

# 인접행렬
graph = [[0] * (N+1) for _ in range(N+1)]
# 인접리스트
graph2 = [[] for _ in range(N+1)]
# 

#방문여부 기록
visited = [0]* (N+1)
# 그래프 연결 초기 셋팅
for _ in range(M):
    start, end = map(int, input().split())
    # 양방향 설정
    graph[start][end]= 1
    graph[end][start]= 1
#탐색전 시작점
# V번 노드 출발
visited[V]= 1
dfs(V)


print(*result)
#--------- bfs -----------
from collections import deque

# N, M, V = map(int, input().split())


# 인접 리스트
# graph = [[] for _ in range(N+1)]
#=>graph = [[], [], [].....]

# 간선 정보 입력
for _ in range(M):
    start, end = map(int, input().split())
    graph2[start].append(end)
    graph2[end].append(start)
    # ex. 1 2
    #     1 3
    # graph[1]=[2], graph[2]=[1]
    # graph[1]=[2, 3], graph[3]=[1]
    # 최종: graph = [[2, 3], [1], [1]]
    
# 정점 순서 정렬도 필요함.
# 현재: [5, 4]이런식
for i in range(1, N + 1):
    graph2[i].sort()


result2 = []
# 함수
def bfs(start):
    #초기화
    dq= deque([start])
    visited = [0] *(N+1)
    visited[start] = 1
    # print(start, end= ' ')
    result2.append(start)
    # dfs 시작- 큐가 빌 때까지 반복
    while dq:
        #  dq에서 앞에 숫자를 빼서 now에 저장
        now = dq.popleft()
        
        # 꺼낸 now를 가지고 연결노드 찾기
        for next_node in graph2[now]:
            # 이미 방문한 노드면 다음으로
            if visited[next_node]:
                continue
            # 아니라면
            # 해당 노드 출력하고
            # print(next_node, end= ' ')
            result2.append(next_node)
            #방문처리
            visited[next_node] = 1
            dq.append(next_node) # 연결된 

bfs(V)

print(*result2)


