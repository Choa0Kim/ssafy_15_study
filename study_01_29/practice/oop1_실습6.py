# main.py
# 요구사항
# 현재 클래스는 초기화 메서드를 가지고, 가로세로 길이를 인자로 받음
# + calculate_are라는 인스턴스 메서드를 추가해서 사각형의 넓이를 구하는 기능 부여
# + calculate_perimeter라는 인스턴스 메서드를 추가해서 사각형의 둘레를 구하는 기능 부여


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



# + 파이썬에서 변수와 객체를 나누는 기준
# 객체: 실제 메로리가 존재하는 데이터 덩어리
# 변수: 이름표

# shape1이라는 인스턴스가 생성되었고, 이 객체는 넓이 5, 높이 3을 가짐
shape1 = Shape(5, 3)
# perimeter1이라는 변수가 생성되었고, shape1의 정보로 calculate_perimeter()한 결과를 담고있음
perimeter1 = shape1.calculate_perimeter()
# perimeter1 변수의 결과를 출력
print(perimeter1)




