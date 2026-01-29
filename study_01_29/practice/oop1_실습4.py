# main.py
# 요구사항
# 현재 클래스는 초기화 메서드를 가지고, 가로세로 길이를 인자로 받음



# 아래 클래스를 수정하시오.

class Shape:
    # 현재 클래스 함수가 필요한가???


    # 초기화 메서드: __init__ 함수
    # - 인스턴스 변수 설정.
    def __init__(self, width, height):  # 가로, 세로 길이를 인자로 설정
        self.width = width
        self.height = height


    def shape_print(self):   
        print(self.width, self.height)



    

# 1. shape1이라는 객체가 생성되었고, 이 객체는 넓이 5, 높이 3을 출력
# 2. 즉, Shape 클래스는 넓이, 높이를 출력시키는 인스턴스 메서드가필요
shape1 = Shape(5, 3)  # 객체 정의만되고 출력은 X, print필요
print(shape1.width, shape1.height)

