
# ------1. 복사--------
# 파이썬 튜터: 코드 순서 확인 가능

# 참조한다 = 주소를 저장한다.

a = [1, 2, 3]
b = a  # a에 대한 참조를 생성한다.
       # a의 주소를 b에 저장한다.

b[1] = 10 #원본 데이터도 같이 변경된다.
#  위z코드는 복사가 아니라 참조를 한다.
#  a[1]은 변할까? 안 변할까?
# print(a, b)
#
# [1, 2, 3]이라는 값만 복사할 수 없을까?
c = a.copy() # 복사
print(c)
# 참조한다 = 주소를 저장한다.(주소를 그래도 복사)
# 얕은 복사(copy())
# - 1차원까지만 복사가 되는 것. (차원까지만 새로운 객체를 생성)
# - 중첩된 데이터들은 참조로 생성

# import copy도 메모리 먹음
# 깊은 복사(copy.deepcopy())
# - 전체 값을 그대로 복사해서 새롭게 생성

# 리스트를 파라미터로 전달받으면 주소를 복사하게 됨(참조)
# - 함수에서 값을 수정하면, 원본 데이터도 같이 수정

def func(li):
    li[0] = 10  # 참조 edhk li가 같은 리스트를 가리킴.

e = [1, 2, 3]
func(e)
print(e)

# 예제
def func(a):
    a = 10  # 참조 edhk li가 같은 리스트를 가리킴.
  
e = [1, 2, 3]
func(e[0])  #  1이라는 값만 복사. 인덱스로 접근하눈 순간 주소가 아니라 값만 복사
            #  => 원본이 변하지 않음
print(e)  
# [1, 2, 3] vs [10, 2, 3]
#  => [1, 2, 3] 


# ----------- 다양한 입력 (List Comprehension) ---------
A = int() # 문자열
#  문자열 -> 리스트
# a b c -> [a, b, c]
input().split() #공백으로 자르자
# a, b, c -> [a, b, c]
input().split(',') # , 기준으로 자르자

# 좌우 공백을 제거
# "    A B C   "   -> "A B C"
clean = input().strip()
print(clean)

# '3 4 5' -> ["3", "4", "5"] -> [3, 4, 5]
# 처리 과정:
# 1) split() → ["3", "4", "5"]
# 2) map(int, ...) → 정수 변환
# 3) list() → 리스트로 변환
numbers = list(map(int, input().split()))
print(numbers)

# 숫자 N줄로 입력
# 4
# 20
# 30
N = int(input())
arr = [int(input()) for _ in range(N)]
print(arr)


# 문자열 abcde를 [a, b, c, d, e]
word_chars = list(input())
print(word_chars)

# "abc def" -> [[a, b, c], [d, e, f]]
word = list(input())
word = word.split()
print(list(map(list, word)))
# =>
word = list(map(list, input().split()))
print(word)


#  메서드 
# - class 내부네 들어간 함수를 메서드


# class
# - 실제 객체를 만들기 위한 설계도
# - 실제 객체(데이터, 동작(기능)) => 설계도에 모두 작성한다.
# - 설계도를 통해 만든 객체를 "인스턴스" 라고 한다.

#  설계도
# 메서드
# - class 내부에 정의된 함수

# class
# - 실제 객체를 만들기위한 설계도
# - 실제 객체 (데이터, 동작(기능))  --> 설계도에 모두 작성한다.
# - 설계도를 통해 만든 객체를 "인스턴스" 라고 한다.

class Person:
    def __init__(self, age, height, job, money, hobby):
        self.age = age
        self.height = height
        self.job = job
        self.money = money
        self.hobby = hobby

    def introduce(self):
        print(f"저는 {self.age}살이고 직업은 {self.job}입니다.")

# 객체 인스턴스
금기륜 = Person(None, 177.1, "강사", "두쫀쿠2개", "게임")
금기륜.introduce()  # class 내부의 함수 == 메서드라고 부른다.

a = "1 2 3"
a.split()