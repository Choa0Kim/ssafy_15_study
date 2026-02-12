# 문제(10039번)
# 입력은 총 5줄로 이루어져 있고, 원섭이의 점수, 세희의 점수, 상근이의 점수, 숭이의 점수, 강수의 점수가 순서대로 주어진다.
# 점수는 모두 0점 이상, 100점 이하인 5의 배수이다. 따라서, 평균 점수는 항상 정수이다. 
# 40점 미만인 학생들은 항상 40점을 받게 된다.
# 출력
# 첫째 줄에 학생 5명의 평균 점수를 출력한다.

def mean(scores):
    total = 0
    cnt = 0
    for score in scores:
        if score < 40 :
            score = 40
        total += score
        cnt += 1
    return total // cnt    
        
print



print(mean([10, 20, 30, 40, 50])) 