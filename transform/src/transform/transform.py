from extrct.mov import list2df
import pandas as pd

def transform(load_dt):
    read_df = list2df(load_dt=load_dt)
    
    cols = ['movieCd', #영화의 대표코드를 출력합니다.
            'movieNm', #영화명(국문)을 출력합니다.
            'openDt', #영화의 개봉일을 출력합니다.
            'rank', #해당일자의 박스오피스 순위를 출력합니다.
            'showCnt', #해당일자에 상영된 횟수를 출력합니다.
            'audiCnt', #해당일의 관객수를 출력합니다.
            'salesAmt', #해당일의 매출액을 출력합니다.
            'audiAcc', #누적관객수를 출력합니다.
            'salesAcc', #누적매출액을 출력합니다.
            'salesShare', #해당일자 상영작의 매출총액 대비 해당 영화의 매출비율을 출력합니다.
            'load_dt'
            ]
    
    df = read_df[cols]
    
    #데이터타입 변환 
    #df['load_dt'] = pd.to_datetime(df['load_dt'])
    df['month'] = pd.to_datetime(df['load_dt']).dt.month
    df[['rank', 'showCnt', 'audiCnt', 'salesAmt', 'audiAcc', 'salesAcc', 'salesShare']] = df[['rank', 'showCnt', 'audiCnt', 'salesAmt', 'audiAcc', 'salesAcc', 'salesShare']].astype(float).astype(int)
    df = df.sort_values(by='audiCnt', ascending=False)
    return df
