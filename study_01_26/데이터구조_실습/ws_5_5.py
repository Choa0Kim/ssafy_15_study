# 아래 함수를 수정하시오.


# 1. append 버전
# def even_elements(input_list):
#     new_list = []

#     for item in input_list:
#         if item % 2 == 0:
#             new_list.append(item)


#     return new_list
            
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)

# 2. extend 사용버전
def even_elements(my_list):
    result = []

    for i in my_list:
        if i % 2 == 0:
            result.extend([i]) 
        # extend(): 

    return result
            
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
