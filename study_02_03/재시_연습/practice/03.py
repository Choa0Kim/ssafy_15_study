# 리스트 뒤집기
def reverse_list(visited_items):
    arr = []
    n = 0
    for  _ in visited_items:
        n += 1
    for item in range(n-1, -1, -1):
        arr.append(visited_items[item])
    return arr



        
        






print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(['A', 'B', 'C']))  # ['C', 'B', 'A']
#####################################################

