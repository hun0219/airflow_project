# Box Office Data Retrieval
- 이 패키지는 변환된 데이터를 /tmp/load 경로에 parquet파일로 저장하는 작업을 수행합니다. 이 문서에서는 사용 방법, 설치 요구 사항, 그리고 각 함수의 설명을 제공합니다.
  
## 설치 요구 사항
- python 3.9 이상
- https://github.com/play-gogo/transform.git@d2.0.0/test 패키지
이 라이브러리들은 'pip'을 사용하여 설치할 수 있습니다.
```bash
$ pip install git+https://github.com/play-gogo/transform.git@d2.0.0
```

## 설치방법
```python
pip install git+https://github.com/play-gogo/load.git@d2/0.1.0
```

## pdm 가상환경에서 설치방법
```python
pdm add git+https://github.com/play-gogo/load.git@d2/0.1.0
```

## 호출방법
```bash
$ load_data
```
