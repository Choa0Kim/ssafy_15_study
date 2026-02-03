def count_votes(votes_list):
    result_dict = {}
    for vote in votes_list:
        if vote in result_dict:
            result_dict[vote] += 1
        else:
            result_dict[vote] = 1
    max_count = 0
    best_supporter=""  
    for name, count in result_dict.items():
        if  count > max_count:
            max_count = count
            best_supporter = name

    return result_dict, best_supporter    

            


# 테스트 코드
votes_list = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob']
result_dict, best_supporter = count_votes(votes_list)

print(f"전체 투표 결과: {result_dict}")
print(f"이달의 서포터: {best_supporter}")
# 출력 예상:
# 전체 투표 결과: {'Alice': 3, 'Bob': 2, 'Charlie': 1}
# 이달의 서포터: Alice