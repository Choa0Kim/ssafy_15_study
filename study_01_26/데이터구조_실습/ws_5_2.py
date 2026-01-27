# 아래 함수를 수정하시오.

#  중복제거

# - 1. for 문 사용

def remove_duplicates(input_list):
    new_lst = []
    for i in input_list:  
        if i not in new_lst:  #만약 inpu_list에서 꺼낸 i가 new_lst에 없다면
            new_lst.append(i)  # 그 i를 new_lst 에 포함
    return new_lst
        

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5]) 
#  input_list에 인자 값으로 [1, 2, 2, 3, 4, 4, 5]가 들어감.
print(result)

# -2. set -> list 로 변환하는 방법

# def remove_duplicates(input_list):
#     return list(set(input_list))

# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5]) 
# #  input_list에 인자 값으로 [1, 2, 2, 3, 4, 4, 5]가 들어감.
# print(result)
    
