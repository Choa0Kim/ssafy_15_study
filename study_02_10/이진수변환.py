# def recur(num):
#     if num == 0:
#         return 
#     # 짝수일때
#     if num % 2 == 0:
#         print("0")
#         return recur(num//2)  # 2 로 나눈 몫을 전달
#     # 홀수일때
#     if num % 2== 1:
#         print("1")
#         return recur(num//2)
    

# N = int(input())
# result = recur(N)
# print(result)



# 강사님 풀이

def recur(num):
    if num == 0:
        return 
 
    recur(num//2)
    print(num %2, end='')
    
N = int(input())
recur(N)



# # return 형태
# def recur(num):
#     if num == 0:
#         return ""
#     return recur(num // 2) + str(num%2)
    

# N = int(input())
# print(result(N))