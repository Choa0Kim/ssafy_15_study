import sys
sys.stdin = open("input.txt", "r")
# 강사님 풀이
T = 10
for tc in range(1, T + 1):
    arr= input().split()  #문자 그대로 써도 됨. 숫자변경 필요없이
    stack = []
    # 숫자를 보고
    # - 저장되어 있는 곳(==stack)의 마지막 숫자와 현재 숫자 비교
    # 마지막 숫자가 들어있곳 확인
    for num  in arr[1]:
        #1.stack이 비어있으면 숫자를 그냥 넣음
        if len(stack) == 0:
            stack.append(num)       
        #2.stack의 마지막 데이터와 현재 숫자를 비교한다.
        # - 같다면, stack의 마지막 숫자를 제거
        # - 다르다면, stack 에 숫자를 추가
        else:
            if num == stack[-1]:
                stack.pop()
            else:
                stack.append(num)
    print(f'#{tc} {"".join(stack)}')            
        
    

# T = 10
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#     stack = [] # 빈 스택 
#     # print(arr)
#     # arr을 num으로 하나씩 꺼내서 스텍이 담기
#     for num in arr:
#         stack.append(num)
#     # 담겨있는 스텍에서 한 숫자씩 비교
#     # arr의 길이 만큼 반복
#     for i in range(len(arr)):
#         #stack i번째와 i+ 1번째가 같은면
#         if stack[i] == stack[i+1]:
#             # stack에서 제외
#             stack.pop
#         elif stack[i] != stack[i+1]: 
#             continue


#     print(stack)    





    