
# 월말 평가 정보
# 8~10문제: 2시간 시간중요.
# 1,2 문제: min, max 최대, 최소, 길이
# 실버4 난이도:3~4문제
# 온라인 실습 난이도에서 벗어나지 않음
# 재귀호출 1문제
# vscode 사용가능


# 월말 대비 문제
# - 내장함수 사용 없이 구현
#   => min, max, sum, len, count 구현
#   예시1) 최소값과 최대값의 차이를 출력해라
#   예시2)가장 길이가 긴 단어 출력해보가
#   예시3) 짝수만 합하여 출력해보기
#   예시4)이 차원 리스트에서 가장 큰 값 찾기
    # 123
    # 456
    # 780
#  이런식의 입력도 받을 수 있는지

# list, dictionary, set 기초
#  예시1) 두 리스트에 모두 등장하는 값의 개수
#  예시2) 카운팅 관련 문제(백준 문제 참고, 알파벳 관련)
#  예시3) 딕셔너리 리스트에서 평균 점수 구하기
#  예시4) 가장 많아 등장한 값 + 중복제거





# 시간제한
# 1초 라는 시간을 측정할 수 있는 기준이 존재
# C 언어 기준 1초당 연산 1억번
# ptthon 1초당 3천만번
# ex. 
# N :500,000
# m: 500,000
# 2중 for문 =  500,000 X 500,000 => 2중 for 문 불가
# 시간제한, 메모리 제한 => 자료구조와 알고리즘 선택할 때 검증

# --------문자열 집합 
# 1. 단순 리스트 활용
# - in 연산 사용은 느림
# 2중 for문 구조
n, m = map(int, input().split())
# m = int(input())
S = [input() for _ in range(n)]
words = [input() for _ in range(m)] 

count = 0
for word in words:
    # word in S: word가 s안에 있는 지 없는 지 검사
    #  S안의ㅡ 요소들은 한 개씩 다 봄.
    if word in S:
        count += 1
print(count)

# in => 한개씩 다 비교

# ------좀 더 빨리 하는 방법
#  어떤 집합안에 데이터가 있는지 없는지 빠르게 검색
# 

# 2. set 활용
#  - 순서 상관 X / 중복데이터 X --> 집합 내부 요소 검색은 set이 빠름

n, m = map(int, input().split())

S = set()
for _ in range(n):
    S.add(input())

count = 0
for _ in range(m):
    word = input()
    if word in S: # 해싱으로 인해 리스트보다 in 연산이 훨씬 빠름
        count += 1
print(count)











