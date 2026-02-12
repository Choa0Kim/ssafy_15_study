# 문제(10818번)
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
# 예제입력
# 5
# 20 10 35 30 7

# 함수버전
# min_val = scores[0]
# max_val = scores[0]

def min_score(scores):
    min_val = scores[0]
    max_val = scores[0]
    for num in scores:
        if num < min_val:
            min_val = num
    for num2 in scores:
        if num2 > max_val:
            max_val = num2  
    return  min_val, max_val  


print(min_score([20, 10, 35, 30, 7])) #(7, 35)