import pandas as pd
import requests
import os
import json
from pprint import pprint
def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def gen_url(dt="20200101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

def req(load_dt="20200101"):
    url = gen_url(load_dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    return code, data

def req2list(load_dt='20200101') -> list:
    _,data = req(load_dt)
    l=data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def list2df(load_dt='20120101'):
    l = req2list(load_dt)
    df = pd.DataFrame(l)
    df['load_dt']=load_dt
    return df

