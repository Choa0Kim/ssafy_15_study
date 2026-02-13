# 백트레킹
# - 전체 경우의 수(기본 재귀호출)
#   - N 중 for문 형태
# 예시) 주사위 3개 (1,1,1) ~(6,6,6)
# 6^3만큼 경우의 수가 나옴
# 반복문 버전(3중 for문)
# for a in range(1,7):
#     for b in range(1,7):
#         for c in range(1,7):
#             print(a, b, c)
# but, 주사위가 k개 라면 불가. (k개의 반복문이 생김. k개 정해진 경우에 사용)
             
#재귀버전
#k;3
#시작: 주사위를 하나도 안던짐
#끝:주사위 k개를 던지면 끝
#누적값
# - cnt:던진 횟수
# - path: 던진 주사위 기록
# k = 3
# def recur(cnt, path):
#     if cnt == k :
#         print(path)
#         return
    
#     for i in range(1, 7):  
#         path.append(i)
#         recur(cnt + 1, path)
#         path.pop()

# recur(0, [])

    # 함수 안 반복문 과정
    # #1 경우
    # path.pop()  # 마지막을 없애주고 
    # path.append(2)
    # recur(cnt+1, path)
    # #~6까지 반복됨
    # path.pop()
    # path.append(6)
    # recur(cnt+1, path)

    # path.pop()
print('---------------------------')
# - 부분집합
#   - 전체 중 일부만 골라서 문제를 해결
# arr =['A', 'B', 'C', 'D']
# # 전체 부분 집합을 출력하는 재귀함수 
# # 시작: 0개의 데이터를 부분집합에 넣을지 말지 고려
# # 끝: 모든 데이터를 부분집합에 넣을지 말지 고려
# # 누적값
# #   - cnt: 몇 개의 데이터를 고려했는가?
# #   - subset: 현재 부분집합
# def recur2(idx, subset): #   원소의 갯수만큼  ox가 나옴
#     if idx == len(arr):
#         print(subset)
#         return
        
    
#     #1. 현재 원소를 부분집합에 포함
#     subset.append(arr[idx])
#     recur2(idx+1, subset)
#     subset.pop()

#     #2. 현재 원소를 부분집합에 포함 X =>현재 subset을 그래도 넘겨짐
#     recur2(idx + 1, subset) 

# recur2(0, [])



# - 순열
#   - 전체 중 k개를 순서를 고려하면서 골라서 문제를 해결
# - 중복 순열(같은 걸 여러번 골라도 된다)
# aaa~ddd
arr = ['A', 'B', 'C', 'D']
k = 3

# 시작: 0개의 알파벳을 고른 
# 끝: k개의 알파벳을 선택
# 누적값: cnt: 현재까지 고른 알파벳 갯수, path: 현재까지 고른 알파벳
#세자리 수 
# def recur(cnt, path):
#     #종료 조건
#     if cnt == k:
#         print(*path)  #최종 task: 값 출력
#         return
#     # 반복 

#     for i in range(len(arr)) :
#         path.append(arr[i])
#         recur(cnt +1, path)    
#         path.pop()  

# recur(0, [])

# - 순열(중복 허용X)
# - 중복 순열 코드에서 중복을 없애는 코드만 추가
used = [0] * len(arr)

def recur4(cnt, path):
    #종료 조건
    if cnt == k:
        print(*path)  #최종 task: 값 출력
        return
    # 반복 
    for i in range(len(arr)) :
        if used[i]: #이미 i를 사용한 적이 있다면  ㅊ
            continue

        used[i] = 1
        path.append(arr[i])
        recur4(cnt +1, path)    
        path.pop() 
        used[i] = 0 # 쓴적이 없다고 초기화 

recur4(0, [])


# 문자열 경우의수
# def recur(cnt, path):
#     #종료 조건
#     if cnt == k:
#         print(path)  #최종 task: 값 출력
#         return
#     # 반복 

#     for str in arr :
#         path.append(str)
#         recur(cnt +1, path)    
#         path = path[:-1]  #문자열의 뒤자리를 자르기

# recur(0, [])


# - 조합
#   - 전체 중 k개를 골라서 문제 해결


arr = ['A', 'B', 'C', 'D']
K =3
#pre: 이전 선택
def recur5(cnt, pre, path):
    if len(path) == K:
        print(*path)
        return
    # 이전 선택의 다음부터만 선택지로 고려
    for i in range(pre + 1, len(arr)):
        path.append(arr[i])
        #현재 선택인 i를 같이 전달
        recur5(cnt +1, i, path)
        path.pop()

recur5(0, -1, [])

# 2/12-n과m 문제 풀기


