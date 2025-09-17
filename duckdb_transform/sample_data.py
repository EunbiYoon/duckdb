import pandas as pd
import numpy as np

# 랜덤 데이터 개수 
num_rows = 100_000

# 랜덤 날짜 생성 함수
def random_dates(start, end, n):
    date_range = pd.date_range(start=start, end=end)
    return np.random.choice(date_range, n)

# 랜덤 데이터 생성
np.random.seed(42)  # 재현 가능하도록 고정
data = {
    "id": np.arange(1, num_rows + 1),
    "name": np.random.choice(["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"], num_rows),
    "age": np.random.randint(18, 70, num_rows),
    "salary": np.random.randint(30000, 150000, num_rows),
    "department": np.random.choice(["HR", "Engineering", "Marketing", "Sales", "Finance"], num_rows),
    "join_date": random_dates("2000-01-01", "2024-12-31", num_rows).astype(str)  # 범위 내 랜덤 날짜 선택
}

# DataFrame 생성
df = pd.DataFrame(data)

# CSV 저장
df.to_csv("sample_data.csv", index=False)

print("✅ data.csv 파일 생성 완료! (랜덤 데이터 포함)")
