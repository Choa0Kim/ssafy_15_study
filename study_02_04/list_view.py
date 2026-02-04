T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    # arr = [0, 0, 254, 185, 76, 227, 84, 175, 0, 0]
    ans = 0
 
    # 전체 빌딩에 대해 반복
    for i in range(2, len(arr)-2):
 
        # 선택된 현재의 빌딩을 최고의 높이라고 가정
        max_height = arr[i]
        # print(max_height)
        # 현재 높이가 최고임을 보장하는 flag 변수
        is_height = True
        # 중간 최대치 높이를 저장하는 변수
        mid_height = arr[i-2]
        # print(mid_height)
 
        # 앞뒤 2개씩 살펴봐서 최고 높이가 갱신되면 해당 경우는 pass
        for j in range(-2, 3, 1):
            # print(arr[i+j])
            if(arr[i+j] > max_height):
                is_height = False
                break
 
            # 본인 높이를 제외하고, 큰 빌딩의 높이를 구하기
            if(j != 0):
                if(mid_height < arr[i+j]):
                    mid_height = arr[i+j]
 
        # print(mid_height)
        # 최고점이 갱신 되었다면 해당 케이스는 차이를 계산할 필요 없음
        if(not is_height):
            continue
 
        ans += arr[i]-mid_height
        #print(f'{i}번째 빌딩 차이: {arr[i]-mid_height}')
 
 
    print(f'#{test_case} {ans}')        