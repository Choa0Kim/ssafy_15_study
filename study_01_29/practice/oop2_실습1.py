# 주어진 코드가 끝까지 실행 될 수 있도록 try-execpt 문으로 수정하시오.


data = {'name': '홍길동'}
# if not data['age']:
#     print(data['age'])
# else:
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)

try: 
    #  일단 시도
    print(data['age'])
except:
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)



arr = ['반갑', '하세요', '안녕']
# for i in range(4):
#     print(arr.pop())
# print(arr)
# 아래에 코드를 작성하시오.
# 일단 pop 과정 수행

try:
    for i in range(4):
        print(arr.pop())
        # print(arr)    
except: 
    print(arr)   
    print("더 이상 pop 할 수 없습니다.")




word = '3.15'
# print(int(word))


# 아래에 코드를 작성하시오.
try:
    print(int(word))

except:
    print("정수로 변환 가능한 값을 입력해 주세요.")    

