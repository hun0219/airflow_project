from transform.transform import transform
import pandas as pd


def load(load_dt):
    df = transform(load_dt)
    print(df.head(3))   # 상위 3개 행 출력 (내용 확인용)
    
    path = "/root/airflow_project/storage"
    print(f"[LOAD] 저장 {path}")

    df.to_parquet(
        path, 
        partition_cols=['month','load_dt']
        )  #parquet 저장
    print("[LOAD] 저장 완료")
