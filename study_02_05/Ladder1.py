import sys
sys.stdin = open("input.txt", "r")


# 테스트 케이스 고정문제
for _ in range(1, 11):
    tc = int(input())  #테케번호 따로 받기
    # arr로 input받기 
    # 100 x 100행렬
    arr = [list(map(int, input().split())) for _ in range(100)] 

    # 시작점 찾기 
    # 0번 열 부터 99번 열까지 다 출발 시키기(j좌표를 0~99까지 확인)
    for start_j in range(100):
        #근데 현재 위치 값이 0이면
        if arr[0][start_j] == 0:
            continue # 패스
        # 위치를 찾으면 현재 위치 초기화 
        #=> 찾은 곳에서 시작
        i = 0
        j = start_j 

        #바닥에 닿을 때까지 반복(내려가기)
        while i < 99:
            # 시작점에서 바로 오/왼에 1이 있는 지 확인
            # 만약 왼쪽에 1이 있고, 0(배열 밖)이라면
            if j > 0 and arr[i][j-1] == 1 :
                # 길이 끝날 때까지 직진
                # j가 0보다 클때까지(배열밖으로 벗어나지 않을 때까지)
                # and 내려가는 곳이 1인 동안
                while j > 0 and arr[i][j-1] == 1:
                    # 실제로 j가 한 칸씩 왼쪽으로 이동
                    j -= 1
            # 위처럼 오른쪽도 확인 후 계속 이동(오른쪽으로 계속가면 99에 도달)    
            elif j < 99 and arr[i][j+1] == 1:
                while j < 99 and arr[i][j+1] == 1:
                    j += 1
            # 옆으로 다 갔으면 아래로 한 칸
            i += 1
        # 바닥도착
        if arr[99][j] == 2:
            print(f'#{tc} {start_j}')    
            break



        
    











    