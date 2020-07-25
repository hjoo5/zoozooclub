# 1. code purpose
- soundcloud에서 download가 가능한 곡들을 다운로드합니다.

# 2. file description
## 2.1 h_utils.py
- json 파일을 만들고 불러오는 용도의 함수가 포함되어있습니다.

## 2.2 makingChartList.py
- ChartList.json을 만드는 파일입니다.
- chartList 변수는 chart를 key로 갖는 딕셔너리 타입 변수입니다.
```python
chartList.keys()
```
> dict_keys(['top50', 'newHot'])

- 각 chart는 23개의 genre를 key로 갖는 딕셔너리 타입 변수입니다.
```python
chartList['newHot'].keys()
```
> dict_keys(['ambient', 'allMusic', 'alterRock', 'classical', 'country', 'danceedm', 'dancehall', 'deephouse', 'disco', 'drumbass', 'dubstep', 'eletronic', 'folkSingersongwriter', 'hiphopRap', 'house', 'indie', 'jazzBlues', 'metal', 'pop', 'rbSoul', 'rock', 'soundtrack', 'world'])

- 각 gerne는 url, cnt_download, link, songTitle, singer를 key로 갖는 딕셔너리 타입 변수입니다.
	- url: 해당 차트의 해당 장르의 url을 value로 갖습니다.
	- cnt_download: 초기값은 0이며 노래 한 곡을 다운로드 받을 때 1씩 증가하여, 결과적으로 다운로드 한 노래의 수를 count합니다.
	- link: 초기에는 빈 리스트이며 크롤링을 진행하면 해당 차트의 해당 장르의 곡들의 링크를 추가하는 리스트입니다.
	- songTitle: 초기에는 빈 리스트이며 크롤링을 진행하면 해당 차트의 해당 장르의 곡들의 노래제목을 추가하는 리스트입니다.
	- singer: 초기에는 빈 리스트이며 크롤링을 진행하면 해당 차트의 해당 장르의 곡들의 가수이름을 추가하는 리스트입니다.
```python
chartList['top50']['rbSoul'].keys()
```
> dict_keys(['url', 'cnt_download', 'link', 'songTitle', 'singer'])

## 2.3 chartList.json
- makingChartList를 실행시키면 얻을 수 있는 json 파일입니다.
- 이 json 파일을 linkSongSingerCrawling에서 불러와 크롤링을 진행합니다.

## 2.4 linkSongSingerCrawling_ver_03.py
- 중간중간 주석을 달았습니다.
