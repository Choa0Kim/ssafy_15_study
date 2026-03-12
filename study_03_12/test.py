import sys
sys.stdin = open("input.txt", "r")

# 1차원 배열만 사용하여 메모리 사용 줄인 버전
# 퀸을 놓을 수 있는지 검시하는 함수
def check(row):
    for prev_row in range(row): # 현재 행(row) 이전의 모든 행들을 검사
        # 1. 세로체크. 같은 열에 퀸이 있는 지 확인
        if visited[row] == visited[prev_row]:
            return False

        # 2. 대각선 체크
        #  행의 차이와 열의 차이가 같아야. 대각선에 있을 수 있음.
        # => |r1-r2|= |c1-c2|/ abs()=> 절댓값 구하는 함수
        if abs(row- prev_row) == abs(visited[row] - visited[prev_row]):
            return False
    # 위 두 조건을 모두 통과하면 안전한 자리    
    return True    

# 한 행씩 내려가면서 퀸을 놓을 수 있는 모든 경우의 수 탐색
def recur(row):
    global cnt  
    #1. 모든 행에 퀸을 다 놓은 경우
    if row == N:
        cnt += 1 # 유효한 조합을 하나 찾았으므로 카운트 증가
        return
    # 현재 행에서 모든 열을 하나씩 시도
    for col in range(N):
        visited[row] = col #현재 행의 col번째 자리에 퀸을 놓았다고 가정

        # 퀸을 놓ㅇ른 자리가 인전한지 확인
        if not check(row):
            continue  # 안전하지 않으면 다음 열(col)로 넘어감 (가지치기)

        # 안전하다면 다음행(row+1)으로 넘어기서 다시 퀸을 놓음
        recur(row+1)


# 실행 및 출력
T = int(input())

for tc in range(1, 1+T):

    N = int(input())

    # visited[행] = 열 ex. visited[0]= 2 : 0행 2열에 퀸이 있음.
    visited = [0] * N   
    cnt = 0 # 정답 갯수 기록 변수

    recur(0) #0번부터 시작
    print(f'#{tc} {cnt}')


