def sum_row_maximums(matrix):
    max_total = 0
    for num in matrix:
        max_val = num[0]
        for n in num:
            if n > max_val:
                max_val = n
        max_total += max_val 

    return max_total          





print(sum_row_maximums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # 18
print(sum_row_maximums([[-1, -2, -3], [-10, -5, -1], [-100, -200, -300]])) # -102
print(sum_row_maximums([[5]])) # 5