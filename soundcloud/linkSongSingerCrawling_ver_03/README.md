# code purpose
- soundcloud에서 download가 가능한 곡들을 다운로드합니다.

# file description
## h_utils.py
- json 파일을 만들고 불러오는 용도의 함수가 포함되어있습니다.
## makingChartList.py
- ChartList.json을 만드는 파일입니다.
- chartList 변수는 chart를 key로 갖는 딕셔너리 타입 변수입니다.
```python
chartList.keys()
```
dict_keys(['top50', 'newHot'])
- 각 chart는 23개의 genre를 key로 갖는 딕셔너리 타입 변수입니다.
```python
chartList['newHot'].keys()
```
dict_keys(['ambient', 'allMusic', 'alterRock', 'classical', 'country', 'danceedm', 'dancehall', 'deephouse', 'disco', 'drumbass', 'dubstep', 'eletronic', 'folkSingersongwriter', 'hiphopRap', 'house', 'indie', 'jazzBlues', 'metal', 'pop', 'rbSoul', 'rock', 'soundtrack', 'world'])
- 각 gerne는 
## chartList.json
- makingChartList를 실행시키면 얻을 수 있는 json 파일입니다.
- 이 json 파일을 linkSongSingerCrawling에서 불러와 크롤링을 진행합니다.
## linkSongSingerCrawling_ver_03.py
