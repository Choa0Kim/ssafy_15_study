# dat 연습 - 성실한 직원 찾기
# dat: 리스트의 인덱스에 의미부여

T = int(input())

# 테스트 케이스를 반복
# 2차원 리스트 입력 받기
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    count_dat = [0] * 10000001  #+1로 설정, 올 수 있는 모든 사원번호
    # 이차원 리스트 인덱스 문으로 접근
    for i in range(H): #세로
        for j in range(W): #가로
            target = matrix[i][j] # 사번 위치
            count_dat[target] += 1  # 사번 호출 갯수

    # 메서드 안 쓰고 최대값, 위치 -> 반복문 index 기준  
    max_count = count_dat[0]
    
    for i in range(10000001):
        #i번째 사원이 현재 max_count 보다 많이 왔다면
        if count_dat[i] >= max_count: #같을 때도 초기화.
            max_count = count_dat[i]
            max_index = i

    # print(max_count)

#     # 메서드 안쓰고 최대값 위치

#     # max_count = max(count_dat)  #최대값
#     # max_index =count_dat.index(max_count)  #최대값 위치

# print(f'#{tc} {max_index}')

# #  딕셔너리로 구현
# T = int(input())
# H, W = map(int, input().split())
# # 빈딕셔너리 생성
# arr = {}
# for key, value in arr.items():
#     print(arr)
   




#  + 
    # print(max_count)
    # # 이차원 리스트 값 직접 접근
    # for row in matrix:
    #     for num in row:

# 내일 dat 응용, 블랙리스트 문제 



T = int(input())

# # 테스트케이스를 반복
for tc in range(1, T + 1):
    # 가로, 세로 값 받기
    T = int(input())
    H, W = map(int, input().split())
    #  빈 딕셔너리 만들기
    arr = {}
    # H(세로)만큼 반복
    for i in range(H):
        #한 줄을 리스트로 받아서 하나씩 딕셔너리에 넣는 과정
        if arr in arr[i]:
            arr[i] += 1
        else: 
            arr[i] = 1
        
        k, v = map(int, input().split())
        #  떼어낸 k, y를 arr 딕셔너리에 넣기
        for k, y in arr.items():
            if 


    #  받은 딕셔너리에서 
  







#  - 사원 중에서 성실 직원을 찾는 문제
#  - 성실 직원: 가장 많이 출근한 사람
#   -> 출근한 횟수를 비교
# - 출근한 횟수를 어딘가 저장해야 한다
#   - list : 10,000,001 개를 만들어야 함
#   - dictionary : 7개만 만들면 됨
# - 사원 번호를 하나씩 보면서 카운팅
# - 가장 큰 수, 인덱스

