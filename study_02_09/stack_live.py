# 간단한 스택
top = -1
stack = [0] * 10

# push 1
top += 1
stack[top] = 1
# push 2
top += 1
stack[top] = 2
# push 3
top += 1
stack[top] = 3

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])


txt = input()
# 스택생성
top = -1
stack  [0]  * 100  #입력 최대 길이
for x in txt:
    if x == '(':
        top += 1
        stack[top] = '('

    elif x == ')':
        if top == -1: # 여는 괄호 없으면 오류
            print('Error')
        else:            # 여느 괄호 없으면 pop
            top -= 1   
            # 괄호가 여러 종류면 이 부분에서 비교
            # if stack[top+1] == '(' and x != ')' :
            #     break
            # elif stack[top+1] == '{' and x ==

 #
 # 
 # 
 # 
def check_parenthesis(text):
    stack = []  # 빈 스택 생성
    # text안에 한 글자를 char로 지정해서 판별
    for char in text:
        # 만약 char에 여는 괄호가 있다면,
        if char == '(':
            # 1. 여는 괄호는 무조건 Push
            # stack에 해당 글자를 append
            stack.append(char)
        # 닫는 괄호면     
        elif char == ')':
            # 2. 닫는 괄호가 나왔는데 스택이 비어있다면?
            if len(stack) == 0:
                return False  # 실패: 닫는 괄호가 너무 많음 '())'
            
            # 3. 짝이 맞으므로 스택에서 제거 (Pop)
            stack.pop()

    # 4. 모든 처리가 끝난 후 스택이 비어있는지 확인
    if len(stack) > 0:
        return False  # 실패: 여는 괄호가 남음 '(()'
    else:
        return True   # 성공: 깔끔하게 비어있음

# 테스트
print(check_parenthesis("(())"))   # True
print(check_parenthesis("(()"))    # False (여는 것 남음)
print(check_parenthesis("())"))    # False (닫는 것 과잉)
print(check_parenthesis(")("))     # False (시작부터 닫음)




