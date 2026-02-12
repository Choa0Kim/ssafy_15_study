#  ---------내 풀이-리스트 활용

# S = str(input())


# def count(S):

#     a = 'a'
#     z = 'z'
#     #  26개의 리스트 만들기(a~z:26개)
    
#     arr =[0] * 26
#     # char: S의 한글자씩 
#     for char in S:
#         # arr에 인덱스 순서부여
#         #  a-a=0, b-a=1 # 모든 char를 a로 나눠주면 각 알파벳의 자리를 알수있음
#         index = ord(char) - ord('a')  
#         #  char가 a~z사이에 있다면: 소문자 알파벳이라면
#         if 'a'<= char <='z':
#             # arr에 + 1 
#             arr[index] += 1
#         else: 
#             arr[index] += 0
#     return arr

# result = count(S)
# print(*result)

# ord(): 아스키 코드 알려주는 메서드


# 순서가 중요하면 set()은 사용X


# # ------------강사님 풀이 1
# S = input()
# di = {}

# # a ~ z 가 0개인 상태로 초기화
# for w in range(ord('a'), ord('z') + 1):
#     di[chr(w)] = 0

# # S 에서 알파벳을 하나씩 COUNTING
# for w in S:
#     di[w] += 1

# for v in di.values():
#     print(v, end=' ')

# ---------------강사님 풀이 2 , defaultdict 활용

# from collections import defaultdict

# S = input()
# di = {}

# for w in S:
#     di[w] += 1
# for w in range(ord('a'), ord('z') + 1):
#     print(di[chr(w)], end=' ')



# ----------- 강사님 풀이 3, 리스트(DAT)
# DAT : 인덱스에게 나만의 의미를 부여해서 활용하는 방법 
# 26개로 지정되어잇음: 리스트로 가능.




S = input()
count_list = [0] *26

for w in S:
    count_list[ord(w) - ord('a')] += 1

print(*count_list)  # *로 언패킹하여 출력(f-string안에서는 사용 불가)

