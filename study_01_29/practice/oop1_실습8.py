# main.py
# 요구사항
# 현재 클래스는 초기화 메서드를 가지고, 가로세로 길이를 인자로 받음
# + calculate_are라는 인스턴스 메서드를 추가해서 사각형의 넓이를 구하는 기능 부여
# + calculate_perimeter라는 인스턴스 메서드를 추가해서 사각형의 둘레를 구하는 기능 부여
# + print_info 라는 인스턴스 메서드를 추가해서 사각형의 가로, 세로, 넓이를 출력하는 기능 부여
#   => 단순 return이 아니라 print까지 필요


class Shape:
    # 현재 클래스 함수가 필요한가???


    # 초기화 메서드: __init__ 함수
    # - 인스턴스 변수 설정.
    def __init__(self, width, height):  # 가로, 세로 길이를 인자로 설정
        self.width = width
        self.height = height

        

    # -----인스턴스 메서드-----
    # - 특정 객체(인스턴스)가 수행하는 동작

    # 가로, 높이를 출력하는 인스턴스 메서드
    def shape_print(self):   
        print(self.width, self.height)

    # 넓이를 계산하는 인스턴스 메서드
    def calculate_area(self): # (self): 초기화 함수(__init__에서 인자를 가져오기 때문에)
        return self.width * self.height
    
    # 둘레를 계산하는 인스턴스 메서드
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
    
    # 사격형 정보를 출력하는 인스턴스 메서드 
    def print_info(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()

        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {area}")  #함수안에서 만들었기 때문에 self.은 제외
        print(f"Perimeter: {perimeter}")
        
    # ------- 매직 메서드(던더 메서드) ---------
    # - _init__ 처럼 객체가 태어나자마자 자동으로 실행되는 메서드
    # - ex)print(shape1)하면 자동으로 실행됨.

    # 인스턴스를 문자열로 표현하는 매직 메서드
    def __str__(self):
        # print아니고 return으로 돌려줘야 함.
        # print를 하면 출력만하고 값을 건네주지 않음.
        return f"Shape: width={self.width}, height={self.height}"


# shape1이라는 인스턴스가 생성되었고, 이 객체는 넓이 5, 높이 3을 가짐
shape1 = Shape(5, 3)

print(shape1)
# shape1의 정보를 가지고 print_info()를 실행
# shape1.print_info()

