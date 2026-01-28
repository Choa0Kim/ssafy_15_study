class Myth:
    # 1. 클래스 변수 정의 및 초기화
    type_of_myth = 0  #클래스 변수

    def __init__(self, name):
        # 2.인자로 받은 이름을 인스턴스 변수 name에 할당
        self.name = name
        # 3.인스턴스가 생성( __init__이 호출될 때마다) 숫자 1씩 올림.
        # 앞에 클래스이름(Myth)을 붙여서 클래스 공용임을 명시
        Myth.type_of_myth += 1


    @staticmethod
    # 설명메서드- 신화에 대한 설명 출력/ 딱 설명만 출력
    def description():
        print("신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.")




    
# 인스턴스 생성: 실행
m1 = Myth('dangun')
m2 = Myth('greek & rome')

print(m1.name)
print(m2.name)

print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')




Myth.description()






        
        
