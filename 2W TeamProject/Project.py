#필요한 라이브러리를 불러옵니다.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 한글폰트 사용을 위한 라이브러리

#'Malgun Gothic' 폰트를 사용 설정합니다. (한글 표시 문제 해결)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

#CSV 파일 로드, 다양한 인코딩 시도합니다. 인코딩 오류 대비
try:
    dataframe = pd.read_csv('netflix_titles.csv', encoding='utf-8')
except UnicodeDecodeError:
    try:
        dataframe = pd.read_csv('netflix_titles.csv', encoding='ISO-8859-1')
    except UnicodeDecodeError:
        dataframe = pd.read_csv('netflix_titles.csv', encoding='cp949')

#불필요한 'Unnamed' 컬럼을 제거합니다.
dataframe = dataframe.loc[:, ~dataframe.columns.str.contains('^Unnamed')]

#'director' 컬럼의 결측값을 'Unknown'으로 채웁니다.
dataframe['director'].fillna('Unknown', inplace=True)

#'date_added' 컬럼을 날짜 형식으로 변환합니다.
dataframe['date_added'] = pd.to_datetime(dataframe['date_added'], errors='coerce')

#'listed_in' 컬럼에서 장르 분리 후 explode를 통해 리스트를 풀어낸 후 다시 재구성합니다.
dataframe['listed_in'] = dataframe['listed_in'].str.split(', ')
dataframe = dataframe.explode('listed_in')

#'International Movies'와 'International TV Shows' 범주를 제거합니다.
dataframe_filtered = dataframe[~dataframe['listed_in'].isin(['International Movies', 'International TV Shows'])]

#연도별로 각 장르의 빈도를 계산하여 정리합니다.
genre_by_year_filtered = dataframe_filtered.groupby(['release_year', 'listed_in']).size().unstack(fill_value=0)

#release_year 컬럼의 최소값과 최대값을 확인하여 데이터 범위를 파악합니다.
release_year_range = dataframe_filtered['release_year'].agg(['min', 'max'])
print(release_year_range)

#2024년 데이터의 장르 분포를 확인합니다.
genre_distribution_2024 = genre_by_year_filtered.loc[2024].sort_values(ascending=False)
print(genre_distribution_2024.head())  # 상위 몇 개 장르를 출력하여 확인

#각 연도별 가장 인기 있는 장르와 그 빈도수를 계산합니다.
max_genre_per_year = genre_by_year_filtered.idxmax(axis=1)
max_counts_per_year = genre_by_year_filtered.max(axis=1)


#필요한 데이터만 선택
dataframe_s = dataframe[['release_year', 'type', 'listed_in']]

#'listed_in' 컬럼이 이미 리스트 형태로 데이터가 주어져 있으므로, 그대로 확장
genres_expanded = dataframe_s.explode('listed_in')

#'listed_in' 컬럼명을 'listed_genres'로 변경
genres_expanded.rename(columns={'listed_in': 'listed_genres'}, inplace=True)

#출시년도와 장르별 작품 수 집계
grouped = genres_expanded.groupby(['release_year', 'listed_genres']).size().reset_index(name='count')

#장르별 총 출현 빈도 계산
genre_counts = genres_expanded['listed_genres'].value_counts()

#Top 10 장르 식별
top_10_genres = genre_counts.head(10).index.tolist()
#Bar Plot
recent_year = genre_by_year_filtered.index.max()
recent_genre_popularity = genre_by_year_filtered.loc[recent_year].sort_values(ascending=False)[:10]
plt.figure(figsize=(12, 6))
sns.barplot(x=recent_genre_popularity.values, y=recent_genre_popularity.index)
plt.title(f'{recent_year}년 가장 인기 있는 장르')
plt.xlabel('빈도')
plt.ylabel('장르')
plt.show()

#인기 장르와 해당 빈도수를 데이터프레임으로 결합합니다.
popular_genre_by_year = pd.DataFrame({
    'Year': max_genre_per_year.index,
    'Genre': max_genre_per_year.values,
    'Count': max_counts_per_year.values
})
plt.figure(figsize=(14, 8))
scatter = sns.scatterplot(data=popular_genre_by_year, x='Year', y='Genre', hue='Genre', size='Count', sizes=(100, 400), palette='viridis')
plt.title('연도별 가장 인기 있는 넷플릭스 장르')
plt.xlabel('연도')
plt.ylabel('장르')
plt.legend(title='장르', bbox_to_anchor=(1.05, 1), loc=2)
plt.grid(True)
plt.show()



#Scatter 그래프 그리기
fig, ax = plt.subplots()
colors = plt.cm.get_cmap('tab20', 10)  # 칼라풀한 색상 10개 준비

for i, genre in enumerate(grouped['listed_genres'].unique()):
    group = grouped[grouped['listed_genres'] == genre]
    if genre in top_10_genres:
        color = colors(top_10_genres.index(genre))
    else:
        color = 'grey'  # 나머지 장르는 회색으로
    ax.scatter(group['release_year'], group['count'], label=genre, color=color)

ax.set_xlabel('Release Year')
ax.set_ylabel('Number of Titles')
ax.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left', ncol=2)
plt.show()