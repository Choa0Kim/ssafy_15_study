import heapq

arr = [20, 15, 19, 4, 13, 11]

#heapq은 최소힙(min_heap)으로 동작함. => 가장 작은 값이 항상 맨 앞으로 옴.

# 하나씩 데이터를 추가하여 최소힙 생성
min_heap = []


for num in arr:
    heapq.heappush(min_heap, num) #arr에서 하나씩 꺼내서 min_heap에 넣을 때마다 알아서 최소값 순서로 정렬

print(min_heap)

# 최대 힙 구현(음수 트릭)
max_heap = []
for num in arr:
    # 파이썬은 최소힙만 지원 => 숫자에 -를 붙여 부호를 바꾸기.
    # -20이 -4보다 작기 때문에 힙의 맨 앞으로 가게됨
    heapq.heappush(max_heap, -num)
# heappop(): 가장 앞의 것을 꺼냄.
while max_heap:
    pop_num = heapq.heappop(max_heap)

    print(-pop_num, end=' ')

