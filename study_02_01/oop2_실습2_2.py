# 아래 클래스를 수정하시오.

class Animal:
    # num_of_animal의 클래스 속성 정의
    num_of_animal = 0
    def __init__(self):
        pass
        

class Dog(Animal):
    def __init__(self):
        super().__init__()
        Animal.num_of_animal += 1

    
    def bark(self):
        print("멍멍!")


dog1 = Dog()
dog1.bark()

# print(f"현재 동물의 수: {Animal.num_of_animal}")
