# 필요한 라이브러리를 임포트합니다.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm # 한글폰트사용을 위한 라이브러리
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# 'Malgun Gothic' 폰트를 사용합니다.
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

# CSV 파일을 로드합니다. 다양한 인코딩을 시도하여 에러를 방지합니다.
try:
    dataframe = pd.read_csv('Customers_Data.csv', encoding='utf-8')
except UnicodeDecodeError:
    try:
        dataframe = pd.read_csv('Customers_Data.csv', encoding='ISO-8859-1')
    except UnicodeDecodeError:
        dataframe = pd.read_csv('Customers_Data.csv', encoding='cp949')



# 데이터의 첫 5행을 출력하여 로드가 정상적으로 되었는지 확인합니다.
print(dataframe.head())

# 데이터의 각 컬럼의 데이터 타입과 결측치를 확인합니다.
print(dataframe.dtypes)
print(dataframe.isnull().sum())

# 각 컬럼의 고유값 개수를 출력합니다.
print(dataframe.nunique())

# 연간소득에서 '$'와 ','를 제거하고 정수형으로 변환합니다.
dataframe['연간소득'] = dataframe['AnnualIncome'].replace('[\$,]', '', regex=True).astype(int)
dataframe.drop('AnnualIncome', axis=1, inplace=True)

# 한글 컬럼명으로 데이터셋의 컬럼 이름을 바꿉니다.
dataframe.rename(columns={'MaritalStatus': '결혼상태', 'EducationLevel': '학력수준', 'Occupation': '직업'}, inplace=True)

# 범주형 변수를 숫자형으로 인코딩하는 함수입니다.
def encode_all_categorical(df):
    for column in df.columns:
        if df[column].dtype == 'object':  # 데이터 타입이 'object'인 경우 (문자형 데이터)
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column].astype(str))  # 문자형 데이터를 숫자형 데이터로 변환
    return df

# 전체 데이터셋에 대한 인코딩 처리
dataframe = encode_all_categorical(dataframe)

# 상관관계 분석을 위한 데이터를 준비하고 상관계수를 계산합니다.
correlation_data = dataframe[['결혼상태', '학력수준', '직업', '연간소득']]
correlation_matrix = correlation_data.corr()
print(correlation_matrix)

# 상관계수 행렬을 시각화합니다.
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()

# 범주형 데이터와 수치형 데이터 간의 관계를 시각화합니다.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
sns.boxplot(x='학력수준', y='연간소득', data=dataframe, ax=axes[0])
axes[0].set_title('학력수준별 소득 분포')
axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0)
sns.boxplot(x='직업', y='연간소득', data=dataframe, ax=axes[1])
axes[1].set_title('직업별 소득 분포')
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0)
plt.tight_layout()
plt.show()

# DecisionTreeClassifier 모델을 생성합니다.
tree_model = DecisionTreeClassifier(random_state=42)

# '결혼상태'를 레이블로 사용하고 나머지는 특성 데이터로 사용합니다.
features = dataframe.drop('결혼상태', axis=1)
labels = dataframe['결혼상태']

# 데이터를 훈련 세트와 테스트 세트로 분할합니다.
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# 모델을 훈련 데이터로 학습시킵니다.
tree_model.fit(X_train, y_train)

# 성능 평가
accuracy = tree_model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")