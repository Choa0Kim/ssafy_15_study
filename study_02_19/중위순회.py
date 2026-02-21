import sys
sys.stdin = open("input.txt", "r")
#전위순회
def recur(node):
    # 자식이 없다면 되돌아가기
    if node == -1:
        return
    # graph[node][0] 왼쪽
    # graph[node][1] 오른쪽

    recur(graph[node][0]) # 왼쪽 자식으로 이동 

    # print(node, end=' ')##현재 노드를 출력(중위순회)
    inorder.append(char_list[node])

    recur(graph[node][1]) # 오른쪽 자식으로 이동

T = 10
for tc in range(1, 1+T):
        info = input()
        if not info: 
             break
        N = int(info)
        # 문자열 저장 배열
        char_list = [0] * (N+1)
        #인접리스트 
        graph = [[-1, -1] for _ in range(N+1)]
        #인접리스트 입력 받기
        for _ in range(N):
            info = input().split()
            idx = int(info[0])  # 노드번호
            char_list[idx] = info[1]  #해당 노드의 문자 저장

            #자식노드에 번호가 있는지 확인
            if len(info) >= 3:
                graph[idx][0] = int(info[2]) # 왼쪽 자식
            if len(info) == 4:
                graph[idx][1] = int(info[3]) # 오른쪽 자식

        inorder = []
        # postorder = []

        recur(1)
        print(f'#{tc} {"".join(inorder)}')
        # print(*inorder)

 