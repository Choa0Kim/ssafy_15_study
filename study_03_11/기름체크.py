import sys
sys.stdin = open("input.txt", "r")

# 전체 데이터 중에서 '#'이 끝나는 지점(경계선) 찾는 이진탐색 함수
def binary_search():
    # 검색할 범위 지정
    # 왼(시작) -> 오(끝)
    left = 0 #검색 시작점
    right = len(oil)-1 #검색 끝점
    
    # 탐색 범위가 남아있는 동안 계솓 반복
    # left(시작점)이 right(끝점)보다 커지면 더이상 확인할 데이터(범위)가 없는 것. 
    while left <= right :
      # 중간 지점 인덱스를 계산
      mid = (left + right) //2

    # 문자열에서 작거나 같은 개념이 없음.
    # => dil[mid] 가 # 아니면 오른쪽을 탐색

      # 중간 지점의 값이 #이라면 아직 뒤에  #이 더 남아있다고 판단.
      if oil[mid] == '#' :
        # 그래서 mid에서 한 칸 뒷쪽(오른쪽)으로 옮겨서 더 탐색
        left = mid +1
      # 만약 중간 지점이 #이 아니라면 더 앞쪽(왼쪽)을 탐색 해야겠다고 판단.
      else:
        # 그래서 끝점을 더 앞쪽(왼쪽)으로 옮김
        right = mid -1
    # 반복문이 끝나면 left는 #이 끝나는 바로 다음 지점에 위치
    return int(left *100/len(oil))        
      
  
T = int(input())

for tc in range(1, 1+T):
  oil = input().strip()
  result = binary_search()
  print(f'#{tc} {result}%')





  
  



  
  