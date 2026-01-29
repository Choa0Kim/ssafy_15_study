# 📘 Python Object-Oriented Programming (OOP) 학습 정리

이 저장소는 파이썬의 클래스 상속, 메서드 재정의(Overriding), 그리고 다중 상속에서의 MRO(Method Resolution Order) 규칙을 실습하고 정리한 공간입니다.

---

## 🚀 학습 목표
- 클래스 상속을 통한 코드 재사용성 이해
- `super()` 키워드를 활용한 부모 클래스 자원 접근
- `@staticmethod`와 `@classmethod`의 차이점 및 활용법 숙지
- 다중 상속 시 발생하는 MRO(메서드 탐색 순서) 구조 파악

---

## 🏗 클래스 설계 구조



### 1. Employee (최상위 부모 클래스)
- **속성**: `name`, `department`
- **클래스 변수**: `employee_count` (인스턴스가 생성될 때마다 전체 직원 수 카운트)
- **주요 메서드**:
  - `introduce()`: 기본적인 자기소개 출력.
  - `mz_introduce()`: `self.introduce()`를 호출한 뒤 추가 정보를 출력하는 확장형 메서드.
  - `@staticmethod check_validate()`: 객체 상태와 상관없이 부서 유효성을 검사하는 유틸리티 함수.
  - `@classmethod get_employee_count()`: 클래스 변수에 접근하여 현재 총인원을 출력.

### 2. Developer & Designer (자식 클래스)
- **특징**: 부모 클래스를 상속받아 각각 `language`와 `tool`이라는 전용 속성을 추가.
- **메서드 오버라이딩**: `introduce()`를 재정의하여 각 직무의 특성을 출력하되, `super().introduce()`를 통해 부모의 로직을 재사용함.

### 3. FullStackDeveloper (다중 상속)
- `Developer`와 `Designer`를 동시에 상속.
- **초기화 전략**: 다중 상속 시 발생할 수 있는 `super()`의 복잡성을 피하기 위해 `Employee.__init__(self, name, department)`를 직접 호출하여 공통 조상을 초기화함.

---

## 🔍 핵심 개념: MRO (Method Resolution Order)

다중 상속 시 파이썬이 메서드를 찾는 순서는 매우 중요합니다. `FullStackDeveloper`의 경우 다음과 같은 순서로 탐색이 진행됩니다.

**MRO 탐색 순서:**
1. `FullStackDeveloper` (본인)
2. `Developer` (상속 리스트의 첫 번째)
3. `Designer` (상속 리스트의 두 번째)
4. `Employee` (공통 부모)
5. `object` (모든 파이썬 클래스의 최상위 객체)

> **Tip:** `print(FullStackDeveloper.__mro__)`를 통해 실제 튜플 형태의 탐색 순서를 확인할 수 있습니다.

---

## 💡 상속 설계 가이드라인
1. **단일 상속 지향**: 클래스 계층 구조가 너무 깊어지거나 복잡해지지 않도록 가급적 단일 상속을 기반으로 설계합니다.
2. **다이아몬드 상속 주의**: 여러 부모가 동일한 조상을 가질 경우(다이아몬드 구조), `super()`의 동작 원리를 정확히 이해하고 설계해야 합니다.
3. **Mixin 활용**: 기능을 조각처럼 추가하고 싶을 때는 `Mixin` 클래스를 만들어 다중 상속으로 결합하는 방식을 권장합니다.

---

## 🛠 실행 예시
코드 실행 시 `Employee.employee_count`가 인스턴스 종류(Employee, Developer, Designer 등)에 상관없이 통합되어 관리되는 것을 확인할 수 있습니다.