## 프로젝트 전에 먼저 duckdb를 설치하기
- brew install duckdb
- pip install -r requirements.txt

## VS code 에서 파일 읽기
- parquet : parquet-viewer
- orc : run read_orc.py

## 프로젝트 실행 : duckdb와 아래의 데이터 처리 방식을 이용해서 csv data를 parquet, orc형태로 변형하기
- arrow
- pandas

## ORC vs. Parquet vs. CSV 비교
| 형식  | 저장 방식          | 압축률 | 속도(읽기) | 속도(쓰기) | 빅데이터 최적화 |
|-------|-----------------|--------|------------|------------|--------------|
| CSV   | 행 기반 (Row)   | 낮음   | 느림       | 빠름       | ❌           |
| ORC   | 컬럼 기반 (Columnar) | 높음   | 빠름       | 보통       | ✅           |
| Parquet | 컬럼 기반 (Columnar) | 중간   | 빠름       | 보통       | ✅           |
- ORC와 Parquet은 컬럼 저장 방식으로 CSV보다 읽기 속도가 빠르며, 빅데이터 분석에 최적화되어 있습니다.
- ORC는 반복되는 데이터에서는 압축효과가 작음.
- 속도는 ORC가 미세하게 더 빠름

## run transformer.py
[[[ ⏳ 파일 쓰기 성능 비교 ]]]
- 📌 Arrow → Parquet 저장 완료: 0.058 초
- 📌 Pandas → Parquet 저장 완료: 0.077 초
- 📌 Arrow → ORC 저장 완료: 0.013 초
- 📌 Pandas → ORC 저장 완료: 0.013 초

[[[ 📊 저장된 파일 크기 비교 ]]]
- 💾 Arrow → Parquet : 0.2 MB
- 💾 Pandas → Parquet : 0.2 MB
- 💾 Arrow → ORC : 7.0 MB
- 💾 Pandas → ORC : 7.0 MB

[[[ ⏳ 저장된 파일 읽기 성능 비교 ]]]
- 📖 Arrow → Parquet 읽기 시간: 0.016 초
- 📖 Pandas → Parquet 읽기 시간: 0.007 초
- 📖 Arrow → ORC 읽기 시간: 0.007 초
- 📖 Pandas → ORC 읽기 시간: 0.011 초

## 결론
- 압축룔 : Parquet (0.2MB) > ORC (7.0MB) vs CSV (8.1MB)
- 속도 (읽기 + 쓰기) : Parquet(0.074초) < ORC (0.02초)