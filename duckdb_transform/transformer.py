import time
import duckdb
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.orc as orc
import pandas as pd
import os

# 파일 쓰기 함수
def write_file(read_csv):
    # 파일 쓰기 시간 비교
    print("\n[[[ ⏳ 파일 쓰기 성능 비교 ]]]")

    # CSV 로드 완료 시간 측정
    start_time = time.time()

    ###### Arrow Table -> Parquet ######
    arrow_table = read_csv.to_arrow_table()
    pq.write_table(arrow_table, "result/data_arrow.parquet")
    arrow_parquet_time = time.time() - start_time
    print(f"📌 Arrow → Parquet 저장 완료: {arrow_parquet_time:.3f} 초")

    ###### Pandas -> Arrow -> Parquet ######
    start_time = time.time()
    pandas_dataframe = read_csv.to_df()
    wrap_pandas = pa.Table.from_pandas(pandas_dataframe)
    pq.write_table(wrap_pandas, "result/data_pandas.parquet")
    pandas_parquet_time = time.time() - start_time
    print(f"📌 Pandas → Parquet 저장 완료: {pandas_parquet_time:.3f} 초")

    ###### Arrow Table -> ORC ######
    start_time = time.time()
    orc.write_table(arrow_table, "result/data_arrow.orc")
    arrow_orc_time = time.time() - start_time
    print(f"📌 Arrow → ORC 저장 완료: {arrow_orc_time:.3f} 초")

    ###### Pandas -> Arrow -> ORC ######
    start_time = time.time()
    orc.write_table(wrap_pandas, "result/data_pandas.orc")
    pandas_orc_time = time.time() - start_time
    print(f"📌 Pandas → ORC 저장 완료: {pandas_orc_time:.3f} 초")

    # 저장된 파일 크기 출력
    print("\n[[[ 📊 저장된 파일 크기 비교 ]]]")
    print(f"💾 Arrow → Parquet : {os.path.getsize('result/data_arrow.parquet') / (1024 * 1024):.1f} MB")
    print(f"💾 Pandas → Parquet : {os.path.getsize('result/data_pandas.parquet') / (1024 * 1024):.1f} MB")
    print(f"💾 Arrow → ORC : {os.path.getsize('result/data_arrow.orc') / (1024 * 1024):.1f} MB")
    print(f"💾 Pandas → ORC : {os.path.getsize('result/data_pandas.orc') / (1024 * 1024):.1f} MB")

# 파일 읽기 함수
def read_file():
    # 저장된 파일 읽기 성능 비교
    print("\n[[[ ⏳ 저장된 파일 읽기 성능 비교 ]]]")

    # Arrow → Parquet 읽기 시간 측정
    start_time = time.time()
    pq.read_table("result/data_arrow.parquet")
    arrow_parquet_read_time = time.time() - start_time
    print(f"📖 Arrow → Parquet 읽기 시간: {arrow_parquet_read_time:.3f} 초")

    # Pandas → Parquet 읽기 시간 측정
    start_time = time.time()
    pd.read_parquet("result/data_pandas.parquet")
    pandas_parquet_read_time = time.time() - start_time
    print(f"📖 Pandas → Parquet 읽기 시간: {pandas_parquet_read_time:.3f} 초")

    # Arrow → ORC 읽기 시간 측정
    start_time = time.time()
    orc.read_table("result/data_arrow.orc")
    arrow_orc_read_time = time.time() - start_time
    print(f"📖 Arrow → ORC 읽기 시간: {arrow_orc_read_time:.3f} 초")

    # Pandas → ORC 읽기 시간 측정
    start_time = time.time()
    pd.read_orc("result/data_pandas.orc")
    pandas_orc_read_time = time.time() - start_time
    print(f"📖 Pandas → ORC 읽기 시간: {pandas_orc_read_time:.3f} 초\n")


# 평가 함수
def evaluation(read_csv):
    # 파일 쓰기 평가
    write_file(read_csv)
    # 파일 읽기 평가
    read_file()


def main():
    ###### duckdb로 csv 파일 읽어오기 ######
    read_csv = duckdb.query("SELECT * FROM read_csv_auto('data.csv')")
    # 평가 함수 호출
    evaluation(read_csv)


# 이 부분이 메인 함수 실행을 보장
if __name__ == "__main__":
    main()
