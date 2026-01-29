# 사람의 이름과 나이를 입력받아서 소개하는 Person 클래스 정의
# 자신을 소개하는 introduce인스턴스가 포함되어야 함.
# 인스턴스가 생성될 때마다 number_of_people 클래스 변수가 작성되어야 함.

# 아래 클래스를 수정하시오.
class Person:
    # 클래스 변수 지정 및 값 초기화
    number_of_people = 0

    # 초기화 메서드: 인스턴스 변수 설정
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 인스턴스? 클래스가 호출될 떄마다 클래스변수에 += 1
        Person.number_of_people += 1
        
    
    # introduce 메서드 

    def introduce(self):
        return print(f"제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.")
         


person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
