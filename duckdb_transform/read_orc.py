import pyarrow.orc as orc
import pandas as pd

# ORC 파일 경로
file_path = "result/data_arrow.orc"

# ORC 파일 읽기
with open(file_path, 'rb') as f:
    orc_file = orc.ORCFile(f)
    table = orc_file.read()

# PyArrow Table을 Pandas DataFrame으로 변환
df = table.to_pandas()

# DataFrame 출력 (VS Code의 터미널에 결과가 보임)
print(df.head())  # 첫 5개의 데이터 출력
