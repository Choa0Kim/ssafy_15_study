# 이진검색
# 이진검색에서 반드시 만족해야 하는 조건=> 정렬이 되어있어야 함

# 현재 이진 검색으로 풀 수 없는 문데들

#- 중복된 숫자가 존재하는 문제들
# - 범위값 검색
#  - N 이상인 개수
#  - A~B 사이 값을 가진 데이터의 수

# - A가 첫 번째 시작하는 위치
# - A를 초과하는 값이 시작하는 위치

#- 현재: 작거니 같을 때만 탐색 범위를 수정
#- 심화: 특정 조건일 때 탐색 범위를 수정
#   - 검색 키워드: parameric search/ lower bound, upper bound




arr = [7, 4, 2, 9, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용
arr.sort()

def binary_search_while(target):
  left = 0            # 검색 시작점
  right = len(arr)-1  # 검색 끝점
  cnt = 0             # 검색 횟수
  # 교차가 되는 순간이 탐색 못한 순간
  while left <= right:  
    mid = (left + right) // 2
    cnt += 1
    # 정답을 찾으면 종료
    if arr[mid] == target:
      return mid
    
    
    # arr[mid]가 target보다 더 큰 경우 (target이 왼쪽에 위치)
    # => 왼쪽을 탐색해야 함
    if target < arr[mid]:
      right = mid -1
    # arr[mid]가 target보다 더 작은 경우 (target이 오른쪽에 위치)
    # => 오른쪽을 탐색해야 함
    else:
      left = mid + 1
  # 리턴되면 못찾았다는 의미니까? -1    
  return -1, cnt    
targets = [9, 2, 20]

for target in targets:
  result = binary_search_while(target)
  if result == -1:
    print(f'{target}은 배열에 없습니다')
  else:
    print(f'{target}은 {result}위치에 있습니다')

print(f'9 = {binary_search_while(9)}번째 위치')

