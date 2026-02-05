def count_menus(orders):
    #  빈 딕셔너리 생성
    di = {}
    for menu in orders:
        
        if menu in di:
            # di라는 딕셔너리 안에 있는  menu라는 키에 +1
            di[menu] += 1
        else:
            di[menu] = 1
    return di        
            
            
            






print(count_menus(['Ice Americano', 'Latte', 'Ice Americano', 'Mocha', 'Latte']))
# {'Ice Americano': 2, 'Latte': 2, 'Mocha': 1} (순서는 무관)
print(count_menus(['Cocoa', 'Cocoa', 'Cocoa'])) # {'Cocoa': 3}
#####################################################