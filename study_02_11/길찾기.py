
for _ in range(10):    
    t, E = map(int, input().split())
    raw_data = list(map(int, input().split()))

    graph = [[] for _ in range(100)]
    
    
    for i in range(0, len(raw_data), 2):
        start = raw_data[i]
        end = raw_data[i+1]
        graph[start].append(end) # 단방향

    # 방문 기록
    visited = [0] * 100
    
    # 결과 저장 0-실패 1-성공
    result = 0

   
    def dfs(now):
        global result
        # 만약 도착 가능한 경로를 찾았으면 탐색 안함
        if result == 1: 
            return
        
        # 목표 지점 99에 도착하면 끝
        if now == 99:
            result = 1
            return

        # 연결된 다음 장소들 탐색
        for next_node in graph[now]:
            # 방문하지 않은 곳이라면
            if visited[next_node] == 0:
                visited[next_node] = 1  #방문 이력 남기기
                dfs(next_node)         # 다음 노드

    #0번부터 탐색
    dfs(0)
    
    print(f"#{t} {result}")