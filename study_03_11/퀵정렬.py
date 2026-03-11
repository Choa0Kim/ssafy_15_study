# 퀵 정렬

# 피벗: 제일 왼쪽 요소
# 이미 정렬된 배열이나 역순으로 정렬된 배열에서 최악의 성능을 보일 수 있음.
def hoare_partition(left, right):
  pivot = arr[left]
  i = left +1
  j = right
  while i <= j: #교차되면 끝
    # i는 pivot보다 큰 값을 검색(작거나 같은면 i += 1)
    while i <= j and arr[i] <= pivot: 
      i += 1

    # j는 pivot보다 작 값을 검색(작거나 같은면 i -= 1)
    while i <= j and arr[j] >= pivot:
      j -= 1

    if i <j: #swap
      arr[i], arr[j] = arr[j], arr[i]

  # pivot과 j 위치를 swap
  arr[left], arr[j] = arr[i], arr[left]    
  return j


def quick_sort(left, right):
  if left < right:
    pivot = hoare_partition(left, right)
    quick_sort(left, pivot -1)
    quick_sort(pivot + 1, right)

quick_sort(0, len(arr)-1)   
print(arr)

arr = [7, 4, 2, 9, 11, 23, 19]
