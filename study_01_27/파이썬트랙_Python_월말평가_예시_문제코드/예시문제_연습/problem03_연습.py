############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):
    # 유저 id와 pw를 지정
    user_id = user_data['id']
    user_pw = user_data['password']
    for i in user_data:
        # id나 pw가 하나라도 ''이 있으면
        if user_id == '' or user_pw == '':
            # False
            result = False
        # 아니라면, True   
        else: 
            result = True

    return result   
         



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################