# 아래 함수를 수정하시오.
def capitalize_words(input_words):
    #  words_list에 ['hello,', 'world!']로 단어를 쪼갬.
    words_list = input_words.split()
    # new_list 대문자로 바꾼 단어들 담을 리스트 정의
    new_list = []
    
    for words in words_list:
        # capitalize(): 문자열 첫 글자만 대문자만 변환
        new_list.append(words.capitalize())
    # 바뀐 단어들을 다시 공백을 넣어 하나로 합침
    return " ".join(new_list)
    


result = capitalize_words("hello, world!")
print(result)


