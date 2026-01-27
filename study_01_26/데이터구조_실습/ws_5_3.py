# 아래 함수를 수정하시오.
def sort_tuple(input_tuple):
    new_tuple = sorted(input_tuple) # input_tuple을 정렬해서 new_tuple에 넣기
    

    return tuple(new_tuple)   #위 new_tuple은 리스트 형태임. tuple로 변환 필요

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
