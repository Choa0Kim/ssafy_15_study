# T = 10


def dfs(node):
    # 최종 task: [start][end] = 1인지 출력 없으면 0
    print(result)
    # 현재 방문할 수 있는 노드들 방문
    for next_node in range(1, N+1):
        #갈 수 없는 노드는 pass
        if 
# for tc in range(1, T+1):
tc, N = map(int,input().split())
arr = list(map(int, input().split()))
ch1 = [0] * 100
ch2 = [0] * 100
visited = [0] * 100


# 입력이 0 1 0 2 1 4 ...이런식
# (start, end): (0,1) (0,2) (1,4) 이런식 
# => 홀수번째가 시작점, 짝수번째가 끝점임
# 그래프 초기 셋팅
for i in range(0, N+1, 2): # 2칸씩 점프해서 값 확인: 입력받은 배열의 짝수번째 값만 확인
    u = arr[i] # 노드(시작점)번호(이름) 지정 - 노드는 0부터 있으니까
    v = arr[i+1]  # 값(끝점)지정 #짝수번째 값
    # 그래프에 값 채우기
    
    # 입력값이 아직 없는 경우
    if ch1[u] == 0: 
        ch1[u] = v
    # 이미 입력값이 있는 경우
    else:
        ch2[u] = v
# # 단방향 설정
# ch1[start][end] = 1
# ch2[start][end] = 1        

# 출발지에서 시작 방문체크
visited[0] = 1

dfs(0)


