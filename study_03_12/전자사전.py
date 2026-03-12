# 전자사전 예제
import heapq
# 튜플 사용해서 다중 우선순위 
# heapq에 튜플에 넣으면 인덱스 0번부터 차례대로 비교. => 0번값아 같으면 1번 값을 비교.


# 1. 길이 순서로 먼저 출력
# 2. 길이가 같다면, 사전 순으로 출력

arr = ['apple', 'banana', 'kiwi', 'abcd', 'abca', 'lemon', 'peach', 'grape', 'pear']
dictionary = []
# sort 를 쓰면 아래와 같다.
# 즉, 우선순위가 2가지
# arr.sort(key=lambda x: (len(x), x))


# arr을 하나씩 길어, 단어 형태로 삽입
# 튜플은 앞에서 부터 차례대호 비교. 
for word in arr:
    heapq.heappush(dictionary, (len(word), word))



# 전자사전에서 단어를 하나씩 꺼내기
# 1순위: len(word)가 작은 순서대로
# 2순위: 길이가 같으면 word(철자)가 사전 순으로 빠른 것 부터
print("전자사전 순서:")
# dictionary가 빌 때까지
while dictionary:
    length, word = heapq.heappop(dictionary)
    print(f"{word} (길이: {length})")





