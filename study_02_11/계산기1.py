import sys
sys.stdin = open("input.txt", "r")

#후위표기법
  
def infix_to_postfix(tokens):
    result = []
    oper_stack = []
        # 1. 숫자면 그대로 result에 쌓는다.
    # 2. 연산자라면
    #  - oper_stack이 비어있을 때: oper_stack에 추가
    # - 아닐 때
    #   - 나보다 우선순위가 크거나 같은 연산자들을 result로 이동 후 추가

    for token in tokens:
        if token.isdigit():
            result.append(token)
        else:
            if oper_stack:
                result.append(oper_stack.pop())

            oper_stack.append(token)  
    result.append(oper_stack.pop())  #남은 연산자 하나
    return result 
        

    
def get_result(tokens):
    stack = []
    #숫자라면 그냥 stack 에 넣기
    # 연산자라면, stack 에서 숫자 2개 꺼내서 계산 후 다시 넣기
    for token in tokens:
        if token.isdigit():
            #계산하기 위해서 int로 변환하여 넣자
            stack.append(int(token))
        else:
            num1 = stack.pop()    
            num2 = stack.pop()  

            stack.append(num1 + num2)

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    # 후위 표기법으로 변환
    postfix = infix_to_postfix(row)
    # 계산
    result = get_result(postfix)
    
    print(f'#{tc} {result}')



