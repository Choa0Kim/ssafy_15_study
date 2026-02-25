
arr =[]
# 입력 받기
for _ in range(9):
    N = int(input())
    arr.append(N)
# print(arr)
#flg변수 생성
a = True    
# 정렬하고 시작
arr_sort = sorted(arr)
# 해당 범인 값 저장 변수
idx1 =0
idx2 =0
# 전체 값 깔고 시작
total= sum(arr_sort)
# print(total)
# 0~9까지 돌면서 
for i in range(0, 9):
    # total에서 i번째 값 빼기
    total -= arr_sort[i]
    # 해당 인덱스의 값 저장
    idx1 = arr_sort[i]
    # 한 명을 뺀 상태로 나머지 8명을 차례로 빼기
    for j in range(1,9):
        total -= arr_sort[j]
        idx2 = arr_sort[j]
        # 두 명 뺐을 때, total이 100이면 
        if total == 100: 
            # flg변수 변경 => 전체 for문 브레이크 신호
            a = False
            break
        # total이 100이 아니라면, 해당 j번째 값을 빼기 전으로 초기화(i번째 값만 빠진 상태로)
        total +=arr_sort[j] 
    # 안쪽 for 문에서 break 하면 바깥 for문도 break=> flg 변수 활용    
    if a == False:    
        break
    # 해당 i번째가 아니라면 다음 i+1번째를 돌리기 위해 해당 i번째를 빼기 전으로 초기화
    total += arr_sort[i]

# 해당하는 것들만 출력
# print(idx1, idx2)
for i in range(0,9):
    if arr_sort[i] != idx1 and  arr_sort[i] !=  idx2:
        print(arr_sort[i])


        
    