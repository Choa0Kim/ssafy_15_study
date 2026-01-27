# 아래 함수를 수정하시오.
def find_min_max(input_lst):
    #  최소/최대값 리스트
    min_num = input_lst[0]
    max_num = input_lst[0]

    for num in input_lst:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
        

    return (min_num, max_num)



result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
