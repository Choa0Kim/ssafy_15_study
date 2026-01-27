############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 함수 min 함수를 사용하지 않습니다.
def min_score(scores):
    # scores의 0번째(1번째) 값을 min_val에 집어넣음
    # min_val = scores[]=> 인덱스 에러 발생.
    min_val = scores[0]
    # scores에서 숫자하나씩 꺼내서 num이라고 부르고 비교
    for num in scores:
        # scores 에서 꺼낸 num이 min_val보다 작으면 
        if num < min_val:
            # min_val에 가장 최소값을 갱신.
            min_val = num  
        # return min_val  return 위치 주의.
        # if문 안에 있으면 루프가 한 번만 돌고 끝남.
    # for문을 돌리고 최종적으로 최소값을 반환      
    return min_val  #return 위치 주의




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 45
#####################################################

# 테스트 코드는 이곳에
print(min_score([100, 100]))  