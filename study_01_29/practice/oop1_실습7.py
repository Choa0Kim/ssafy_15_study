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
    

    
    # 의문1. 변수를 만들어서 끌어오는 방법도 가능한가? 
    #        => 가능. 초기화메서드에서 설정해서 가져올 수 있음.
    #           다시 의문. 클래스밖에 있는 변수도 가능한가?
    #                   => 가능. global도 가능. 근데 비추천: 클래스는 독립적이여야 하는데, 밖의 변수에 의존되면 
                        #    같은 코드를 다른 파일을 쓰려고 할때, 밖에 변수가 없으면 에러남. + 버그 잡기도 어려움
    # 의문2. 함수안에 함수를 끌어올 수 있나?
            # => 가능. are = self.calculate_area 식으로 사용가능.
            # 다시의문. 함수안에 새 변수를 생성하면 초기화 변수에도 설정해야 하나?
            # => 놉. 

    # 사격형 정보를 출력하는 인스턴스 메서드 
    def print_info(self):
        area = self.calculate_area()
        perimeter = self.calculate_perimeter()

        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {area}")  #함수안에서 만들었기 때문에 self.은 제외
        print(f"Perimeter: {perimeter}")
        

    # + 함수안에서 만든 변수를 다른 함수에 또 쓰고 싶으면
    # self.area = self.calculate_area()로 설정하면 됨.


# + 파이썬에서 변수와 객체를 나누는 기준
# 객체: 실제 메로리가 존재하는 데이터 덩어리
# 변수: 이름표


# shape1이라는 인스턴스가 생성되었고, 이 객체는 넓이 5, 높이 3을 가짐
shape1 = Shape(5, 3)
# shape1의 정보를 가지고 print_info()를 실행
shape1.print_info()

