# ------------- 다중상속 ----------
# - 다중 상속할 때는, 밑에서부터 하나씩 모두 탐색하면서 




VALID_DEPARTMENTS = ("개발팀", "디자인팀", "기획팀")


class Employee:
    company_name = "서울 6반"
    employee_count = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Employee.employee_count += 1

    def introduce(self):
        print(f"안녕하세요, {self.department} 부서 {self.name} 입니다.")

    def mz_introduce(self):
        self.introduce()
        print("MBTI는 INTJ 입니다.")

    @staticmethod
    def check_validate(employee):
        if employee.department in VALID_DEPARTMENTS:
            print("유효성 정상")
        else:
            print("잘못된 입력!")

    @classmethod
    def get_employee_count(cls):
        print(f'총인원 : {cls.employee_count}')


# 개발자(이름, 부서, 언어)
class Developer(Employee):
    def __init__(self, name, department, language):
        super().__init__(name, department)
        # super() 가 Designer를 가리키고 있음

        self.language = language
  
    def introduce(self):
        super().introduce()
        print(f"가장 자신있는 언어는 {self.language} 입니다.")
    

# 디자이너 (이름, 부서, tool)
class Designer(Employee):
    def __init__(self, name, department, tool):
        super().__init__(name, department)

        self.tool = tool

    def introduce(self):
        print(f"안녕하세요 디자이널 {self.name} 입니다.")
        print(f"{self.tool} 을 잘 다룹니다.")


# ======== 다중 상속============
# 풀스택(이름, 부서, 언어, 툴) 
class FullStackDeveloper(Developer, Designer):
    # MRO + super로 인한 버그를 어떻게 최소화할까?
    # - 공통 조상(Employee)만 한 번 초기화, 자식 전용만 따로 설정
    def __init__(self, name, department, language, tool):
        Employee.__init__(name, department)
        self.language = language
        self.tool = tool



# 직원1: (철수, 개발팀)
emp1 = Employee("철수", "개발팀")
emp1.check_validate(emp1)
Employee.check_validate(emp1)
emp1.introduce()

# 직원2: (영희, 디자인팀)
emp2 = Employee("영희", "디자인비슷한팀")
emp2.check_validate(emp2)
emp2.introduce()
Employee.get_employee_count()


# -------------------------------

# 개발자
dev1 = Developer("김개발", "개발팀", "python")
dev1.introduce()

Employee.get_employee_count()

print(Developer.__mro__)


des1 = Designer("최디자인", "디자인팀", "포토샵")
des1.introduce()



fs1 = FullStackDeveloper('박풀스택', '기획팀', 'python', '포토샵')
fs1.introduce()



print(FullStackDeveloper).__mro__

# ------------------------------

# MRO 규칙 -> class 을 어떤 순서로 탐색할까 ?
# - 다중 상속할 때는, 밑에서부터 하나씩 모두 탐색하면서 올라옴

# 예시 (Developer 를 시작으로 호출하면 super 는 누구일까 ?)
# dev1 = Developer("김개발", "개발팀", "python")

# 이 때 MRO 순서는 ?

# 1. Developer
# 2. Employee

# 예시 (FullStackDeveloper 를 시작으로 호출하면 super 는 누구일까 ?)
# fs1 = FullStackDeveloper("박풀스택", "기획팀", "???")

# 이 때 MRO 순서는 ?

# 1. FullStackDeveloper
# 2. Developer
# 3. Designer
# 4. Employee

# --------------------------------

# 상속 설계의 기본 틀
# - 최대한 단일 상속을 기반으로 구현
# - 다중 상속이 필요하다면, 다이아몬드 구조가 나오지 않도록 구현
# - 보통 개발 시 Mixin 이라는 이름으로 +A 를 다중상속 받는 구조를 만든다.

# -------------------------------

# mixin 으로 권한 만들어 놓고, 다중상속으로 
#  상속 설계의 기본틀
# - 최대한 단일 상속 기반으로 구현
#  - 다중 상속이 필요하다면, 다이아몬드 구조가 나오지 않도록 구현
#  - 보통 개발 시 Mixin 이라는 보조용 클래스로 