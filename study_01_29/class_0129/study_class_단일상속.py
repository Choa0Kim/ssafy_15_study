# 상속
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


#  상속

# 개발자(이름, 부서, 언어)
class Developer(Employee):
    #  Employee 에 있는 생성자가 아니라,
    #  Developer 만의 생성자를 "재정의" 함.
    def __init__(self, name, department, language):
        # name, department 초기화 + 직원 수 증기
        #  -> 로직은 Employee에도 그대로 작성되어 있다. 
        self.name = name
        self.department = department
        # self.language = language
        # 방법1. Employee.employee_count +=1
        # 방법2. MRO 규칙에서 가장 우선순위가 높은 class의 init을 호출한다.
        super() .__init__(name, department)
        self.language = language



    # 부모가 가진 introduce 함수와 동일한 이름을 정의
    # -> introduce를 재정의
    def introduce(self):
        print(f"안녕하세요, {self.department} 부서 {self.name} 입니다.") 
        super().introduce() #부모인 Employee 의 introduce 를 호출  
        print(f'가장 자신있는 언어는 {self.language} 입니다.')



    
# 디자이너
class Designer(Employee):
    # tool이라는 인자를 더 쓸거기 때문에, 생성자도 재정의 필요
    # def __init__(self, tool):   #super()로 부모 초기화 메서드인자를 상속해와도 다 인자로 받아야함 
    def __init__(self, name, department, tool):
        super().__init__(name, department)
        self.tool = tool

    #  introduce 메서드를 재정의 했다.
    def introduce(self):
        print(f"안녕하세요, {self.department} 부서 {self.name} 입니다.") 
        print(f'가장 자신있는 도구는 {self.tool} 입니다.')


        # return super().introduce()   



# 직원1: (철수, 개발팀)
emp1 = Employee("철수", "개발팀")
emp1.check_validate(emp1)
Employee.check_validate(emp1)
emp1.introduce()

# 직원2: (영희, 디자인팀)
emp2 = Employee("영희", "디자인비슷한팀")
emp2.check_validate(emp2)
emp2.introduce()

# Employee.get_employee_count()

# -----------------
# 개발자1
dev1 =Developer("김개발", "개발팀", "python")
# 부모의 인스턴트 메서드인 introduce()를 사용가능.
dev1.introduce()

#  방법 1or 2를 하지 않으면
# 총 인원수는 개발자1을 제외한 2명이 나옴.
# Employee.get_employee_count()

#  ------------------
# 디자이너 1
des1=Designer("김화백", "디자인팀", "포토샵")
des1.introduce()

Employee.get_employee_count()





# 순서 확인
# (<class '__main__.Developer'>, <class '__main__.Employee'>, <class 'object'>)
# print(Developer.__mro__)
