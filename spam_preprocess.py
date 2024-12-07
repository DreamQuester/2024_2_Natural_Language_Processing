import pandas as pd

df = pd.read_csv('휴대전화 스팸트랩 문자 수집 내역.csv')

# 7번째 열만 선택하기 (0부터 시작하는 인덱스이므로 6으로 접근)
df_filtered = df.iloc[:, [6]]  # 7번째 열을 선택

# 첫 번째 열에 모두 0 삽입 및 열 이름 변경
df_filtered.insert(0, 'label', 0)  # 첫 번째 열 이름을 'label'로 설정
df_filtered.columns = ['label', 'data']  # 두 번째 열 이름을 'data'로 설정

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
df_filtered.to_csv('spam_data.csv', index=False)