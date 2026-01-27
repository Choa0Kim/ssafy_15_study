# 긴 단어 input(5637번)

all_words = []

while True:
    line = input().split() #line에 공백단위로 끊어서 집어 넣기(문자열)
    if not line: continue # 빈 줄 입력시 무시
    
    if line[-1] == "E-N-D":
        all_words.extend(line[:-1]) #end를 제외한 나머지 추가
        break
    else:
        all_words.extend(line) #line 전체 추가

# 긴 단어 찾기
# str요소 하나씩 접근    
# 기본 값 셋팅
max_word = ""  # 빈 문자열
max_len = 0 

for word in all_words:
    cnt = 0
    for c in word: # 단어에 한글자 씩 돌때마다 
        cnt += 1  # cnt에 +1 (글자길이 세기)
    if cnt > max_len:  # 현재 글자수가 max보다 길면
        max_len = cnt   #max를 현재 글자수로 갱신
        max_word = word  # 현재 단어를 Max_word로 갱신

print(max_word.lower())





