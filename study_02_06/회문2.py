# import sys
# sys.stdin = open("input2.txt", "r")

# arr과 뒤집은 arr이 같은지 비교하는 함수
def is_palindrome(arr):
    return arr == arr[::-1]
# t = 10
for _ in range(1, 11):
    tc = int(input().strip())
    arr = list(input().strip() for _ in range(100))
    zip_arr = list(map("".join, zip(*arr)))  #세로를 가로로 변환
    # 1. *arr : arr안에 있는 문자열을 각각의 인자로 풀기
    # 2. zip(): 풀어 놓은 100개의 인자 행에서 같은 인덱스에 있는 문자들끼리 튜플로 만듦.
    # 3. map("".join): 튜플을 다시 하나의 문자열로 합침.
    
    
    found = False
    # 길이를 100부터 역순으로 확인(가장 길이가 긴 것부터)
    # ex. 90에서 찾으면 더 낮은 길이는 탐색 필요X
    for length in range(100, 0, -1):
        if found: 
            break
            # 줄(1) 루프
        for i in range(100): #0부터 99행까지 탐색
            if found: 
                break
            # 시작점(j)루프
            for j in range(100 - length + 1): #0열부터 (100- length)열까지 탐색
                
                # 가로 검사
                # i행의 j점부터 length만큼 잘라서 회문인지 확인.
                if is_palindrome(arr[i][j:j+length]):
                    print(f"#{tc} {length}")
                    found = True #가로에서 찾으면 break
                    break  
                # 세로 검사 (가로에서 못 찾았을 경우에만 의미가 있음)
                if is_palindrome(zip_arr[i][j:j+length]):
                    print(f"#{tc} {length}")
                    found = True
                    break
              



