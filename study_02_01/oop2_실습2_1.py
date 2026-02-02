# 아래 클래스를 수정하시오.
class Animal:
    # num_of_animal의 클래스 속성 정의
    num_of_animal = 0
    def __init__(self):
        pass
        

    
class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1
    


class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    @classmethod # 현 메서드가 인스턴스 수준이 아니라 클래스수준에서 실행한다는 것을 알려줌
    def access_num_of_animal(cls):
        # cls.num_of_animal 
        return f"동물의 수는 {cls.num_of_animal}마리 입니다."
        

dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
