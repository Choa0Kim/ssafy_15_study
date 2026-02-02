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



class Cat(Animal):
    def __init__(self):
        super().__init__()
        Animal.num_of_animal += 1

    def meow(self):
        print("야옹!")



# 아래 클래스를 수정하시오.
class Pet(Dog, Cat):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    def play(self):
        print("애완동물과 놀기")

    def make_sound(self):
        print(f"{self.sound}")    
            


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
