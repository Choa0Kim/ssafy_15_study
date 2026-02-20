import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
T = 1
for tc in range(1, 1+T):
    N = int(input())
    #빈 인접리스트 생성
    graph = [[] for _ in range(N-2)]
    # 인접리스트 입력 받기    
    for i in range(1, N-2):
        graph[i].append(i+1)
        graph[i].append(i+2)

# print(graph)



    