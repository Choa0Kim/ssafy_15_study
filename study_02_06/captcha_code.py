#30만 X 30만 => 2중 for문 돌리면 시간초과

import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# N, K = map(int, input().split())
# sample_nums= list(map(int, input().split()))
# pw_nums= list(map(int, input().split()))

# print(N, K, sample_nums, pw_nums)
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    target = list(map(int, input().split()))


    result = 0
    target_idx = 0

    for i in range(N):
        # target 이 가리키고 있는 숫자와, sample

        if arr[i] == target[target_idx]:
            target_idx += 1

        if target_idx:
            pass 


    print(f'#{tc} {result}')    
        


