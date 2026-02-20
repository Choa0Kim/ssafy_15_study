import sys
sys.stdin = open("input2.txt", "r")

#전위순회
def recur(node):
    if node == -1:
        return
    
    # print(node, end=' ') #현재 노드를 출력(전위순회)

    recur(graph[node][0]) # 왼쪽 자식으로 이동 

    # print(node, end=' ') # 중위순회

    recur(graph[node][1]) # 오른쪽 자식으로 이동
    print(node, end=' ') # 후위순회

N = int(input())
    #인접리스트 
graph = [[] for _ in range(N)]
    #인접리스트 입력 받기
for _ in range(N):
    node, left, right = map(int, input().split())
    graph[node].append(left)
    graph[node].append(right)    

print(graph)
recur(1)        