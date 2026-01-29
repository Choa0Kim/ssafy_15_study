
# static 변수/메서드
# 상수는 대문자
VALID_DEPARTMENTS = ("개발팀", "디자인팀", "기획팀")

class Employee:
    # 클래스 변수/메서드 변수
    # - 인스턴스들이 모두 공유하는 변수

    company_name = "서울 6반"
    employee_count = 0


    def __init__(self, name, department):
        self.name = name 
        self.department = department
        Employee.employee_count += 1   # 클래스 변수에 접근



    def introduce(self):
        print(f'안녕하세요, {self.name} 부서 {self.department} 입나다.')


    def mz_introduce(self):
        self.introduce()   
        print("MBTI는 INTJ 입니다.")

# 유효성 검사 메서드 
# 직원의 부서가 정상적으로 입력돠었는 지 체크
# - 반드시  class 안에 정의하지 않아도 정상 동작 (보통 안으로 넣음)
# -반드시 Employee 클래스가 있어야먼 의미가 있는 함수
    @staticmethod   #=> 데코레이터  클래스 안에 없어도 작동하는 함수라는 의미
    def check_validate(employee):
        if employee.department in VALID_DEPARTMENTS:
            print("유효성 정상")
        else:
            print("잘못된 입력")
        
    @classmethod # 해당 메서드는 클래스 변수를 활용하는 메서드
                 # 클래스 자기자신을 전달해주면서 활용
    def get_employee_count(cls):  # 클래스 전달
        # 클래스 변수인 employee_count 를 출력
        print(f'총인원: {cls.employee_count}')






#  데코레이터:
# 나만의 데코레이터 함수
# - func을 전달받아서
def my_calcultor(func):
# - func을 꾸며주고
    def wrapper(*args):
        print("계산기 프로그램 환영합니다.")
        func(*args)
        print("안녕히가세여")


@my_calcultor()
def add(a, b):
    print(f'덧셈 : {a + b}')

@my_calcultor()
def sub(a, b):
    print(f'뺄셈 : {a + b}')

add(3, 5)
sub(10, 20)


    

emp1 = Employee("철수", "개발팀")
emp1.mz_introduce()

emp1.check_validate(emp1)  #인스턴스를 통해서 접근  =>X 스태틱인지 인스턴스 메서드인지 알 수 없음
                             # 인스턴스민이 활용항 수 있는 메서드가 아님.
                            

Employee.check_validate(emp1) #class를 통해서 접근  => O /그래서 클래스를 통해서 접근해야 함
                            # 인스턴스들이 동시에 써애함 => class 통해서 접근해야 함
Employee.get_employee_count()
 
emp2 = Employee("영희", "디자인팀")     







