# 아래 함수를 수정하시오.

#  문장: text , 찾을 문자: target
def count_character(text, target):

    new_list = []
    for words in text:
        if words == target:
            new_list.extend([words])


    return len(new_list)


result = count_character("Hello, World!", "o")
print(result)  # 2
