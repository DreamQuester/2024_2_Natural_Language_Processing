import json
import pandas as pd
import os

# JSON 파일이 있는 폴더 경로
folder_path = 'conversation data'  # 해당 폴더의 경로로 변경

# 대화 데이터 저장할 리스트
dialogues = []

# 데이터 수집 카운터
data_count = 0
max_data_count = 10000  # 최대 데이터 수

# 폴더 내 모든 JSON 파일 읽기
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # 대화 데이터 추출
                for info in data['info']:
                    lines = info['annotations']['lines']
                    
                    for line in lines:
                        # 데이터가 최대 수에 도달하면 종료
                        if data_count >= max_data_count:
                            break
                        
                        # 텍스트 데이터만 저장
                        dialogues.append({
                            'label': 1,  # 첫 번째 열 값
                            'data': line['text'].split(': ', 1)[1]  # 텍스트 데이터만 추출
                        })
                        data_count += 1
                    
                    if data_count >= max_data_count:
                        break
                    
        except Exception as e:
            pass

# DataFrame으로 변환
df_dialogues = pd.DataFrame(dialogues)

# 필요한 열만 선택
df_dialogues = df_dialogues[['label', 'data']]

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
df_dialogues.to_csv('message_data.csv', index=False)