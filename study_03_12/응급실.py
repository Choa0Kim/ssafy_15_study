import heapq

class Patient:
    #1. 초기화 메서드: 객체를 만들 때 정보를 저장
    def __init__ (self, name, criticality, age, arrival_time):
        self.name = name                    #이름
        self.criticality = criticality      #위급도 (1~5, 높을수록 위급)
        self.age = age                      #나이
        self.arrival_time = arrival_time    #도착 시간 (숫자가 작을수록 일찍 옴)



    #2. 매직 메서드 : 인스턴스들의 우선순위를 비교할 때 호출하는 메직 메서드
    # 내가 남(other)보다 작은가>를 정의하는 함수
    # heapq는 내부적으로 "A < B"를 비교하여 가장 작은 값을 맨 앞으로 보냄
    # 즉, 우선순위가 높아야 할 환자를 더 작은값으로 판단하게 로직을 짬.
    def __lt__(self, other):
        # 1순위 - 위급도 체크(내림차순)
        # 내 위급도가 other보다 크면 (>) True 반환 -> 내가 더 작은 게 됨
        # 나와 othrer 이 다르다면
        if self.criticality != other.criticality :
            # 크기 비교  나 > 다른사람 => True 
            return self.criticality > other.criticality
        
        # 2순위 - 나이체크(내림차순)
        # 위급도가 같아면 나이가 더 많은 사람을 작은걸로 판단
        if self.age != other.age :
            return self.age > other.age
        
        # 3순위 - 도착 시간 체크(오름차순)
        # 위급도, 나이까지 같으면 먼저 온 사람 우선
        return self.arrival_time > other.arrival_time
    
    # 3. 출력 형식 정의
    def __repr__(self):
        return f"[{self.name}] 위급:{self.criticality}, 나이:{self.age}, 도착:{self.arrival_time}"
    
# 환자 명단
patients = [
    Patient("김철수", 3, 40, 10),  # 평범한 위급도
    Patient("이영희", 5, 70, 11),  # 매우 위급, 고령 (최우선)
    Patient("박민수", 3, 80, 12),  # 철수와 위급도 같지만 나이가 더 많음
    Patient("최지우", 5, 20, 13),  # 영희와 위급도 같지만 나이가 적음
    Patient("정본캐", 3, 40, 9)  # 철수와 위급도/나이 같지만 더 먼저 옴
]

# 힙 구성
pq = []

for p in patients:
    heapq.heappush(pq, p)

# 진료 순서대로 출력
print("응급실 진료 순서")
while pq:
    print(heapq.heappop(pq))
    
        
        
            
        
