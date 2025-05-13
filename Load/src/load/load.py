from transform.transform import transform
import pandas as pd


def load(load_dt):
    df = transform(load_dt)
    df.to_parquet("~/code/playgogo/storage", partition_cols=['month','load_dt'])
    
