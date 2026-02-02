class Dog:
    sound = "멍멍"


class Cat:
    sound = "야옹"

#  Dog을 먼저 상속
class Pet(Dog, Cat):
    def __str__(self):

        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

pet1 = Pet()
print(pet1)    

#  Cat을 먼저 상속
class Pet(Cat, Dog):
    def __str__(self):

        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

pet2 = Pet()
print(pet2)    
