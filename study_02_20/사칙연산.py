import sys
sys.stdin = open("input.txt","r")


# 후위순회 + 계산 함수
def postorder(node_id):
    #현재 노드의 정보 꺼내오기
    info = tree[node_id]
    #노드 정보 분류하기
    
    # 1. info가 1개면 숫자노드
    if len(info) == 1:
        return int(info[0])

    # 2. info가 3개이면 연산자 + 숫자노드
    operator = info[0] # 연산자 저장
    left = int(info[1]) #왼 저장
    right = int(info[2]) #오 저장

    # 왼쪽 먼저 계산 후 오른쪽 계산 => 후위순회 로직
    left_val = postorder(left)
    right_val = postorder(right)
    # 자식노드들의 결과가 돌아오면 현재 노드의 연산자로 계산
    if operator == '+' :return left_val + right_val
    elif operator == '-':return left_val - right_val
    elif operator == '*':return left_val * right_val
    elif operator == '/':return left_val // right_val


T = 10
for tc in range(1, 1+T):
    N = int(input())
    # 빈 딕셔너리 생성
    tree = {}
    # 딕셔너리로 입력받기
    for _ in range(N):
        # 입력값 각각 입력받기
        line = input().split()
        # 각각 받은 입력값에서 맨 앞 숫자를 노드번호로 지정
        node_id = int(line[0])
        # 노드번호는 key, 나머지 정보는 value로 받기
        tree[node_id] = line[1:]

    # 함수 호출
    result = postorder(1)       
    print(f'#{tc} {result}') 

