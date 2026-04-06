# 백준 2606번

# 컴퓨터 수 => 노드 수  연결되어 있는 컴퓨터 쌍의 수 => 간선 수
# 단 방향?
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

N, M = map(int, input().split())
# graph 생성
graph = [[] for _ in range(N+1)]

#그래프 연결
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v) # 단방향 ...?



# union -find
# - 기본 코드 + 튜닝코드 -> 기초 문제 가능
# -mst 문제 해결 가능

# 코테 union -find
# - 게리맨더링 문제
