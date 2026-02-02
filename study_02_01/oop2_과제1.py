# 아래 함수를 수정하시오.
def check_number(num):
    
    try:
        if num > 0:
            print(f"숫자를 입력하세요: {num}")
            print('양수입니다.')
        if num == 0:
            print(f"숫자를 입력하세요: {num}")
            print('0입니다.')
        
        if num < 0:
            print(f"숫자를 입력하세요: {num}")
            print('음수입니다.')   
        
    except:
            print(f"숫자를 입력하세요: {num}")
            print('잘못된 입력입니다.')   
        


check_number(1)
check_number(0)
check_number(-1)
check_number("a")









