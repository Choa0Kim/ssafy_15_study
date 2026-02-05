
T = int(input())
di = [0, 1, 0 ,-1]
dj = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]* N for _ in range(N)]


    # 초기 설정(시작점 좌표 제시)
    i, j = 0, 0
    dr = 0 # 우방향 시작
    # 9x9만큼 숫자 돌리기
    for num in range(1, N*N +1):
            #현 위치에 현재 숫자 붙임. ([0]으로 되어있는 배열 안에)
            arr[i][j] = num
            # 미래 위치 계산(좌표 값)
            ni = i + di[dr]
            nj = j + dj[dr]
            
            # 방향을 틀어야 하는 순간을 지정
            # 1. 배열 범위안에 있는지 확인
            # ni, nj가 0보다 작을 때(좌표 값 밖), ni, nj가 N보다 크거나 작을 때
            # arr[ni][nj] != 0 :이미 채워진 곳이면 방향 전환
            if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
                # 방향을 바꿔야 함.(dr의 인덱스를 변경)
                dr = (dr + 1) % 4 # 2번째 턴부터는  dr=1(하 방향)
                # 꺽은 방향으로 다시 미래 위치 계산
                ni = i + di[dr]
                nj = j + dj[dr] 
           

            i, j =  ni, nj   
    print(f'#{test_case}')
    for row in arr :
         print(*row)
            
        

            

