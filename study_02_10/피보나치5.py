# 재귀함수의 구성요소 ------------------
# 1. 시작점
# 2. 끝점
# 3. 다음 재귀 호출
#   - 다음 재귀 호출 전
#   - 다음 재귀 호출
#   - 호출 이후 돌아와서

# # 문제1. 1, 2, 3, 4 를 출력하세요 (재귀함수로 구현)
# def recur(num):
#     if num == 5:
#         return

#     print(num)
#     recur(num + 1)

# recur(1)


# print()

# # 문제2. 1, 2, 3, 4, 4, 3, 2 1 를 출력하세요 (재귀함수로 구현)
# def recur(num):
#     if num == 5:
#         return

#     print(num)
#     recur(num + 1)
#     print(num)

# recur(1)

# 앞에서 부터 쌓아나가는 그림 -> 반복문
# 위에서부터 반대로 가는 그림 -> 재귀호출

# 재귀호출은 뒤부터 생각.
# 앞의 숫자를 호출을 통해 구현
#1. 구현식 먼저 만들기 N = (N-1)+(N-2) 
#2.구현식 함수로 만들기: fibo(N) = fibo(N-1) + fibo(N-2)
# fibo(10) = fibo(9) + fibo(8)

# 1. N = (N-1)+(N-2)
# 2. fibo(N) = fibo(N-1) + fibo(N-2) => 이게 결과
def fibo(num):
    # 근데 num이 1이면 -1 =>에러
    if num <= 1:  # num이 1이거나 0이면
        return num  # => 1아님. 1번째 num 자리 수임

    return fibo(num-1) + fibo(num-2)

N = int(input())
result = fibo(N)
print(result)



