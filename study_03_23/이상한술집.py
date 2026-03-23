import sys
sys.stdin = open("input.txt", "r")


from collections import deque

def Topological_sort():
    singer_list = []
    queue = deque()

    # 진입 차수가 0인 노드 queue에 입력
    for n in range(1, len(degree)):
        if degree[n] == 0:
            queue.append(n)
    
    while queue:                            # queue가 빌 때까지 반복
        node = queue.popleft()                  # queue에서 노드 꺼내기
        singer_list.append(node)                # 출연 순서 리스트에 현재 노드 저장
        
        for next_singer in graph[node]:         # 현재 노드에서 갈 수 있는 노드 탐색
            degree[next_singer] -= 1                # 다음 노드의 진입 차수 1 감소 (현재 노드와 연결된 간선을 제거하는 역할)
            if degree[next_singer] == 0:            # 다음 노드의 진입 차수가 0인 경우
                queue.append(next_singer)               # queue에 다음 노드 입력
    
    if len(singer_list) != n:               # 모든 가수의 순서를 확정하지 못한 경우 0 출력
        print(0)
    else:                                   # 모든 가수의 순서를 확정한 경우 순서대로 가수의 번호 출력
        for singer in singer_list:
            print(singer)
    

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)                # 각 노드의 진입 차수 저장

for _ in range(M):
    sequence = list(map(int, input().split()))      # 입력 형태: [가수의 수, 1번 순서 가수, 2번 순서 가수, ...]
    for i in range(1, sequence[0]):
        graph[sequence[i]].append(sequence[i+1])        # 이전 가수의 리스트 공간에 다음 가수의 번호 저장
        degree[sequence[i+1]] += 1                      # 다음 가수의 진입 차수 1 증가
        

Topological_sort()          # 위상 정렬 알고리즘 실행