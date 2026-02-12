
# # --------내 풀이 
n = int(input())
#  공백을 기준으로 문자열 리스트 만들기
cards = list(map(int, input().split()))

m = int(input())
#  공백을 기준으로 문자열 리스트 만들기
m_num = list(map(int, input().split()))
# 답을 담을 빈 딕셔너리 준비
count_dict = {}
# cards에서 하나씩 꺼내기(card)
for card in cards:
    # 만약 카드가 count_dict안에 있다면 
    if card in count_dict:
        # count_dict라는 딕셔너리에 card(현재 숫자)key에 있는 value에 +1
        count_dict[card] += 1
    else:  # 아니라면 딕셔너리에 card(현재 숫자)라는 key를 만들고,
           #  vlaue를 1부터 시작.
        count_dict[card] = 1

print(*(count_dict.get(q, 0) for q in m_num))


# ------- 강사님 풀이
N = int(input())
#  숫자공백 입력 받을 때 사용
nums1 = list(map(int, input().split()))

M =int(input())
nums2 = list(map(int, input().split()))

# counting 딕셔너리 초기화
di = {}

for num in nums1:
    if di.get(num):
        di[num] += 1
    else:
        di[num] = 1

# 카운팅 수 출력 
for num in nums2:
    if di.get(num):
        print(di[num], end=' ')
    else:
        print(0, end=' ')    



