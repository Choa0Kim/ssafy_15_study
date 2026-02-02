class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    # BaseModel의 초기화 함수 인자를 받아오고, autor라는 새로운 인자를 추가로 받음
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
class Other(BaseModel):
    # 부모클래스의 클래스 변수 수정
    TYPE = 'Othrt Model'

    # 부모의 save 메서드의 내용을 무시하고 새로운 문구가 나와야 하는 상황에는
    # super가 아니라 그냥 부모의 save를 호출하고 print문을 다시 작성
    def save(self):
        # super().save()
        print('데이터를 다른 장소에 저장합니다.')

# 1. ExtendedModel은 Novel과 Other 클래스를 다중 상속받아야 한다.    
class ExtendedModel(Novel, Other):
    # ExtendedModel은 새로운 속성 extended_type을 가져야 한다.
    # => 초기화 메서드에 새로운 인자를 받아야 함.
    
    # 다중 상속을 받을떄는 BaseModel.__init__보다는 super()사용
    # 현재 Novel이 부모클래스(BaseModel)를 상속받고 있으므로 super() 사용
    def __init__(self, data_type, title, content, created_at, updated_at, author, extended_type):
        super().__init__(data_type, title, content, created_at, updated_at, author)
        self.extended_type = extended_type
        self.TYPE = data_type
        self.PK = 1


    def display_info(self):
        # BaseModel.PK = 1
        # BaseModel.TYPE = 'Basic Model'
        print(f"PK: {self.PK}, TYPE: {self.TYPE}, Extended Type: {self.extended_type}")

    def save(self):
        print("데이터를 확장해서 저장합니다.") 


# extended_instance라는 새로운 인스턴스 생성
extended_instance = ExtendedModel('Other Model', '제목', '내용', 2026, 2026, '작가', 'Extended Type')
print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
extended_instance.display_info()
extended_instance.save()

