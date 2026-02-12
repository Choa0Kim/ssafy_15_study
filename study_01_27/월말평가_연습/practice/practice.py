# a = 'A' #pc입장에서는 그냥 A라는 문자가 아니라 어떤 숫자로 봄. =<> 아스키 코드


# hash func을 잘못만들면 abc, cac, cba가 다 값은 값으로 나옴
def my_hash(word):
    hash = 0
    for w in word:
        hash += ord(w)

    return hash

print(my_hash('abc')) # 294
print(my_hash('bac')) # 294

# hash func충돌 줄이는 코드

# 1.위치 가중치 주기
# 2. 
# 3. 모듈러 연산 추가


# dictionary : 삽입 순서가 보장
# set: 순서보장(X)



