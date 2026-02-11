# N = int(input())
# mod = 10007
# arr = [0] * 1001
# arr[0] = 1
# arr[1] = 2

# for i in range(2, 1001):
#     arr[i] = (arr[i-1] + arr[i-2]) % mod

# print(arr[N-1])

# 다른방법
N = int(input())
mod = 10007
arr = [0] * 1001
arr[1] = 1
arr[2] = 2

for i in range(3, 1001):
    arr[i] = (arr[i-1] + arr[i-2]) % mod

print(arr[N])