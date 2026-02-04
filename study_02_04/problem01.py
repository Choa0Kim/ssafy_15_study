# import sys
# sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
# arr = [list(map(int, input().split())) for _ in range(5)]
    arr = [[(i*j) for j in range(5)] for i in range(5)]
    max_total = 0
    # arr = []
    for sy in range(5):
        for sx in range(5):
            total = arr[sy][sx]
                # max_total = max(max_total, total)  # 값만 필요하다면
                # 좌표값까지 같이 저장
            if total > max_total:
                    max_total = total
                    # max_y = sy
                    # max_x = sx

    print(f'#{test_case} {max_total}')  


