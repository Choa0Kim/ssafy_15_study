# Day 3 정리: EDA와 Scikit-learn

---

## 0. 데이터 수집 후 ML 파이프라인

### 전체 흐름
1. **데이터 전체 확인** — 구조·크기·원하는 데이터 존재 여부
2. **데이터 분할** — Train / Validation / Test
3. **EDA(탐색적 데이터 분석)** — 본격 모델링 전 데이터 이해
4. **전처리** — 결측치·이상치 처리, 스케일링
5. **모델 학습** — 학습·검증 데이터로 파라미터 확정
6. **평가** — 필요 시 이전 단계로 돌아가 개선

### 데이터 분할 비율
| 구분 | 비율 | 용도 |
|------|------|------|
| **Train** | 60~80% | 오차를 줄이는 방향으로 파라미터 학습 (데이터 많을수록 60%에 가깝게) |
| **Validation** | 10~20% | 하이퍼파라미터 튜닝, 모델 선택, 과적합 탐지 |
| **Test** | 10~20% | 최종 성능 평가 — **딱 한 번만** 사용 |

### 과적합(Overfitting)
- 특정 데이터 분포에만 과도하게 맞춰진 상태
- 학습 데이터에서는 성능 높고, 새 데이터에서는 낮음
- 해결: 정규화, 데이터 증강, 조기 종료(Early Stopping)

---

## 1. EDA (탐색적 데이터 분석)

### 목적
- **데이터 이해**: 분포, 이상치, 결측치 파악
- **특성 선택**: 상관관계 높은 변수 식별
- **전처리 설계**: 표준화·정규화 여부 결정
- **가설 검증**: 시각화로 직관 확인

### 기본 작업
| 작업 | 내용 |
|------|------|
| 기초 통계 | shape, info, describe — 평균·최대·최소·중앙값·분산·표준편차 |
| 결측치 | NaN 개수, 비율 확인 |
| 이상치 | IQR 기반 탐지·제거 |
| 분포 | 히스토그램, box plot, kde |
| 상관관계 | scatter, `df.corr()`, heatmap, pairplot |

### 상관계수 해석 (Pearson r)
- **|r| > 0.7**: 강한 상관
- **0.3 ~ 0.7**: 중간
- **|r| < 0.3**: 약함
- **주의**: 상관 ≠ 인과 — "A와 B가 같이 변한다"일 뿐

### 분산·표준편차
- **분산**: 평균에서 얼마나 퍼져 있는가
- **표준편차**: 퍼진 정도를 원래 단위로 표현 (분산의 제곱근)

---

## 2. 전처리: 표준화 vs 정규화

### 표준화 (Standardization)
- 공식: $z = \frac{x - \mu}{\sigma}$
- 결과: **평균 0, 표준편차 1**
- Scikit-learn: `StandardScaler`
- 경사하강법 수렴·특성 영향력 균등화에 유리

### 정규화 (Normalization)
- 공식: $x' = \frac{x - \min}{\max - \min}$
- 결과: **0~1 스케일**
- Scikit-learn: `MinMaxScaler`

### ⚠️ 테스트 데이터에 fit 금지
- **학습 시 fit한 StandardScaler로 transform만** 적용
- `fit_transform(X_train)` / `transform(X_test)` — test에는 fit 절대 금지
- 테스트 데이터가 표준화에 사용되면 **데이터 누수(data leakage)** 발생

---

## 3. Scikit-learn 기본 패턴

### fit / predict
```python
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### 대표 모델
- **회귀**: `LinearRegression()`
- **분류**: `LogisticRegression()`

### 전처리 파이프라인
```python
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)  # fit 없이 transform만
```

### 데이터 분할
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

---

## 4. 회귀 평가 지표

| 지표 | 의미 |
|------|------|
| **RMSE** | Root Mean Squared Error — 오차의 제곱평균의 제곱근 |
| **MAE** | Mean Absolute Error — 절대 오차의 평균 |
| **R²** | 결정계수 — 0~1, 1에 가까울수록 설명력 높음 |

---

## 5. 분류 평가 지표

### 정확도 (Accuracy)
- 전체 데이터 중 맞게 예측한 비율
- **데이터 불균형 시 활용 어려움** (예: 99% 정상, 1% 암)

### 정밀도 (Precision)
- 모델이 **True라고 예측한 것** 중 실제로 True인 비율

### 재현율 (Recall)
- **실제 True인 데이터** 중 모델이 True라고 예측한 비율

### F1-score
- 정밀도와 재현율의 **조화평균**
- 한쪽에 치우치지 않은 균형 지표

### ROC curve
- 분류 **임계값(threshold)** 변화에 따른 성능 곡선
- 임계값 높음(0.9) → True 예측이 줄어듦
- 임계값 낮음(0.1) → 거의 다 True로 예측
- **ROC-AUC**: 곡선 아래 면적 — 1에 가까울수록 좋음

### 혼동행렬 (Confusion Matrix)
- TP, TN, FP, FN — 정밀도·재현율 계산의 기반

---

## 6. 요약 비교

| 구분 | EDA | 전처리 |
|------|-----|--------|
| 목적 | 탐색·분석 | 모델 입력 전 변환 |
| 시점 | 모델링 전 | 학습 직전 |

| 구분 | 표준화 | 정규화 |
|------|--------|--------|
| 결과 | 평균 0, 표준편차 1 | 0~1 스케일 |
| Scikit-learn | StandardScaler | MinMaxScaler |

| 구분 | 회귀 | 분류 |
|------|------|------|
| 평가 지표 | RMSE, MAE, R² | 정확도, 정밀도, 재현율, F1, ROC-AUC |

---

## 7. 실무 참고

### 바닥부터 학습할 일?
- 거의 없다. **SOTA 모델**을 가져다 쓴다.

### 파인튜닝 (Fine-tuning)
- 이미 학습된 모델의 **파라미터 일부만** 수정
- 우리 상황에 맞게 커스터마이징

### AI 수업의 목표
- 바닥부터 모델 만들기보다 → **AI 전체 학습/활용 과정 이해**
- 개발 시 적용할 수 있는 사람, 이론·실전 경험을 쌓는 것
