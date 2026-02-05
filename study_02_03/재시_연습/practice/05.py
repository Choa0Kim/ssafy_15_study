def count_total_items(warehouse):
    cnt = 0
    for items in warehouse:
        
        for item in items:
            
            if item != 0:
                cnt += 1
    return cnt            















print(count_total_items([[1, 0, 2], [3, 4, 5], [0]]))    # 5
print(count_total_items([[0, 0], [0], [30, 40]]))    # 2

