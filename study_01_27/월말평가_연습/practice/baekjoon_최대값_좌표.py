# 최대값과 그 좌표(2566번)
# 문제
# <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

# 여러줄로 되어 있는 input 받는 로직
# 1. input 받을 빈 리스트 준비
arr = []
# 2. 한줄 씩 돌려면서 
for i in range(9): #9줄이기 때문에
    n = list(map(int, input().split())) # 
    # 1.1: input(): 한 줄을 통째로 문자열로 읽음
    # 1.2: split(): 공백을 기준으로 쪼개서 문자열 리스트 만듦.
    # 1.3: map(int,): 리스트의 모든 문자들을 하나하나 int로 변환(아직 리스트 형태 아님)
    # 1.4: list(): int로 변환된 숫자들을 다시 리스트로 묶어줌.
    arr.append(n)
# print(arr)

max_val = arr[0][0]
x = 0
y = 0
# i는 arr의 길이 만큼 반복(리스트 갯수 만큼)
for i in range(len(arr)):
    for j in range(len(arr[0])): # j는 arr안에 있는 리스트들안의 요소 만큼 반복
        if arr[i][j] > max_val: # arr의(i, j)가 max보다 크다면
            max_val = arr[i][j]  # max는 해당 arr(i, j) 값으로 갱신
            x = i
            y = j

print(max_val)
print(x+1, y+1)  #인덱스는 0부터 시작하므로 +1








