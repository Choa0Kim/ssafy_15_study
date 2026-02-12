#queue
# -가장 앞의 데이터만 활용할 때




#우선순위 큐(priority queue)
# - 큐처럼 돌아가는데, 먼저 꺼내지는 우선순위 있다.

q = [1, 2, 3, 4, 5]
#.pop(0)
#deque

while q:
    print(q.pop(0))

from collections import deque
#deque: 이중 연결 리스트 구조
# - 가장 앞 데이터 제거에 특화
# - 큐 관련 문제들은 deque 으로 풀자
# - [주의] 중간 데이터 활용은 느리다 0(N)

dq = deque()
dq.append(3)
dq.append(2)
dq.append(4)
while dq:
    print(dq.popleft())