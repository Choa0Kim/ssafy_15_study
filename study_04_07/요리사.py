import sys
sys.stdin = open("input.txt", "r")

"""
문제유형: DFS, 백트래킹

1. 각 음식에 들어갈 재료의 종류
->N 개 중 N/2개를 고르는 경우의 수 (기저조건)
A 음식에 절반 재료
B 음식에 절반 재료
-> 재료의 종류(branch)

2.시너지 계산
A 음식 시너지 계산
B 음식 시너지 계산
-> 차이가 가장 작은 케이스를 찾자


"""
def cal_synergy(li):
    total = 0
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            a, b = li[i], li[j]
            total += arr[a][b] + arr[b][a]
    return total

def get_synergy():
    A_list, B_list = [], []
    # i 번째 재료의 visited를 보고, 선택되었다면 A_list, 아니면 B_list에 추가
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)
    return cal_synergy(A_list), cal_synergy(B_list)



# 재귀호출 -> N/2 개를 선택(선택된 재료가 A음식/ 선택 안된 재료가 B음식)
def recur(cnt, prev):
    global min_answer

    if cnt == N // 2:
        # 시너지 계산 코드
        a_total, b_total = get_synergy()
        min_answer = min(min_answer, abs(a_total - b_total)) #최소값 갱신
        return
    
    for num in range(prev+1, N):
        if visited[num]:
            continue
        visited[num] =1
        recur(cnt+1, num)
        visited[num] = 0


T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_answer =21e8
    recur(0,0)
    print(f'#{tc} {min_answer}')
