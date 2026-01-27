# 문제 설명
# 사용자님은 성적 관리 시스템을 개발하고 있습니다. 
# 입력 데이터에는 공백이 섞여 있거나 잘못된 형식의 점수가 포함되어 있습니다.
# 데이터를 정제하고, 유효한 점수를 받은 학생들 중 최저 점수를 찾아내야 합니다.
# 요구사항
# 데이터 정제: 학생의 점수 문자열에 공백이 포함되어 있다면 제거합니다.
# 유효성 검사:점수가 숫자로만 이루어져 있는지 확인합니다. (isdecimal() 활용)점수가
# $0$점 이상 $100$점 이하인지 확인합니다.위의 조건을 만족하지 못하는 데이터는 None으로 처리합니다.
# 최저값 탐색: None이 아닌 유효한 점수들 중에서 가장 낮은 점수를 찾습니다.
# 단, 파이썬 내장 함수 min()을 사용하지 말고 for문과 if문을 활용하여 구현하세요.


            
# 입력데이터
student_records = [
    {'name': '김싸피', 'score': ' 95 '},
    {'name': '이싸피', 'score': '82'},
    {'name': '박싸피', 'score': '가져옴'},
    {'name': '최싸피', 'score': ' -10'},
    {'name': '정싸피', 'score': ' 77'},
    {'name': '강싸피', 'score': '105'},
]
        


def main(student_records):
    # 유효한 성적을 담을 바구니
    vaild_score = []
    #  student_records에서 하나씩 꺼내서 student로 지정해서 비교
    for student in student_records:
        # 1. 데이터 정제- 공백제거(strip())
        raw_score = student['score'].strip()

        # 2. 유효성 검사 - 10진수만 isdecimal()
        # raw_score(socre에서 공백이 제거된 점수(아직 문자열))
        # raw_score이 10진수라면
        if raw_score.isdecimal():
            # 그 raw_score를 int로 변환하여, score_int에 넣기
            score_int = int(raw_score)
            # 만약 score_int(int로 변환된 raw_score)가 0~100 사이라면
            if 0 <= score_int <=100:
                # vaild_score(앞서 만들어 놓은 유효한 성적을 담는 바구니)에
                # 해당 score_int를 추가
                vaild_score.append(score_int)

        # 3. 최저점 탐색 - vaild_score가 비워있지 않은 경우만 실행
        #               -> 유효한 점수가 없으면, 최저점 탐색 불가
        if not vaild_score:
            # vaild_score(유효한 점수)가 없는 경우 None을 리턴
            return [], None
        # vaild_score의 1번째 값은 min_score에 넣음.
        min_score = vaild_score[0]
        for score in vaild_score:
            if score < min_score :
                min_score = score

    return vaild_score, min_score

# 결과 => ([vaild_score], min_score)
    
scores, result = main(student_records)
# print(f'유효한 성적 리스트: {scores}')
# print(f'최저 점수: {result}')
print(main(student_records))
        


        
           
            





# isdecimal(): 문자열이 0~9까지의 십진수로만 구성되어 있는지 확인하는 메서드
# 모두 십진수: True. else: False





# 출력 예시
# 유효한 성적 리스트: [95, 82, 77]
# 최저 점수: 77