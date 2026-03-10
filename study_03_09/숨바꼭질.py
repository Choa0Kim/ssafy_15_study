# swea 초능력인서문제랑 비슷
# max 값크기 (짝수, 홀수랑 다름)
# 초능력자 인서 문제와 비슷하답니다. (swea)
# MAX를 조금 더 크게 (짝수의 경우는 괜찮은데, 홀수의 경우에는)

import sys
from collections import deque


N, K = map(int, input().split())
MAX = 100000 

def bfs(start, target):
    # 초기화 단계
    dq = deque([start])
    visited = [0] * (MAX + 1)
    visited[start] = 1  # 시작 위치를 방문 처리

    # 탐색 루프
    while dq:
        now = dq.popleft()

        # 종료조건) 꺼낸 위치가 목적지와 같다면
        if now == target:
            return visited[now] - 1  # 1을 빼고 최단시간 반환하기

        # 갈 수 있는 3가지 방향 탐색
        for next_node in (now - 1, now + 1, now * 2):
            
            # 범위를 벗어나지 않고 (인덱스 에러 방지)
            # 방문한 적이 없는 곳이라면 (visited가 0이라면)
            if 0 <= next_node <= MAX and not visited[next_node]:
                # 후보군으로 등록하면서, 현재 위치까지 걸린 시간+ 1을 누적 기록 (거리 측정)
                visited[next_node] = visited[now] + 1
                dq.append(next_node)  # 다음 후보군으로 등록


print(bfs(N, K))