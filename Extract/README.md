# Box Office Data Retrieval

- 이 프로젝트는 영화진흥위원회(KOFIC) API를 사용하여 박스오피스 데이터를 가져오고 이를 Pandas 데이터프레임으로 변환하는 작업을 수행합니다. 이 문서에서는 사용 방법, 설치 요구 사항, 그리고 각 함수의 설명을 제공합니다.

## 설치 요구 사항
- python 3.9 이상
- pandas 라이브러리
- requests 라이브러리

이 라이브러리들은 'pip'을 사용하여 설치할 수 있습니다.

```bash
$ pip install pandas requests
```

## 환경 변수 설정
- API 키를 사용하기 위해 환경 변수를 설정해야 합니다. API 키는 영화진흥위원회 API 서비스에서 가입 후 생성할 수 있습니다.

```bash
export MOVIE_API_KEY='your_api_key_here'
```

## 설치방법
```bash
$ pip install git+https://github.com/play-gogo/Extract.git@d2/0.1.0
```

## 가상환경에서 설치방법
```bash
$ pdm add git+https://github.com/play-gogo/Extract.git@d2/0.1.0
```
## 호출방법
```bash
$ data
```
