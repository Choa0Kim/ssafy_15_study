


stack = [5, 2, 3, 4, 1]
# 뒤에서 부터 꺼내기
# while stack:
#     num = stack.pop()
#     print(num)


#예시 문제
# ()()((()))  :괄호가 잘 닫혀있는지 확인 - 스택 사용

# 재귀함수 구현
# - 시작지점
# - 종료지점
# - 누적된 값

arr = [5, 2, 3, 4, 1]
# 1. 5 2 3 4 1 순서대로 출력하는 재귀함수를 구현
# - 시작지점: 인덱스 0
# - 종료지점: 인덱스 4
# - 누적된 값: 인덱스
def recur(idx):
    # if에 탈출조건
    if idx == 4:
        print(arr[idx], end=' ')
        return
    print(arr[idx], end=' ')
    recur(idx + 1) # 다음 인덱스를 전달하면서 다음 재귀호출
recur(0) 
print()   

# 2. 5 2 3 4 1 4 3 2 5
# - 시작지점: 인덱스 0
# - 종료지점: 인덱스 4
# - 누적된 값: 인덱스

def recur2(idx):
    # if에 탈출조건
    if idx == 4:
        print(arr[idx], end=' ')
    
        return
    print(arr[idx], end=' ') # 재귀호출 전
    recur2(idx + 1)          # 다음 재귀 호출
    print(arr[idx], end=' ') # 되돌아오면거 할 작업  

recur2(0)  

