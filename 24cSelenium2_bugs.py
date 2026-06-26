from selenium import webdriver
driver = webdriver.Chrome()

driver.implicitly_wait(5)

import time
time.sleep(5)

url = 'https://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
'''
단수 데이터 고정: tr:nth-child(1)처럼 몇 번째 행인지가 고정되어 버려, 반복문(for)을 돌려도 무조건 1등 데이터만 가져오게 됩니다.
'''

songs = soup.select('#CHARTrealtime > table > tbody > tr')
'''
좋은 선정 방법: 의미 있는 '클래스(Class)'와 '구조' 찾기
웹 디자이너들은 개발할 때 노래 제목, 가수, 앨범 등 각각의 목적에 맞게 이름을 붙여둡니다. 이 고유한 이름(클래스나 ID)을 이용하는 것이 좋습니다.

노래들이 모여있는 행들의 공통점 찾기: 벅스 차트의 각 노래 행들은 모두 <table> 태그 안에 <tr class="...">나 일반 <tr> 구조로 나열되어 있습니다.

선정: table.trackList > tbody > tr (차트 테이블 안의 모든 행들을 통째로 리스트로 가져옴)

행 안에서 고유한 클래스 찾기:

노래 제목은 항상 <p class="title"> 안에 있습니다 ➔ p.title > a

가수 이름은 항상 <p class="artist"> 안에 있습니다 ➔ p.artist > a

앨범 이름은 항상 <a class="album"> 태그입니다 ➔ a.album
'''

for song in songs:
  # 노래제목 #CHARTrealtime > table > tbody > tr:nth-child(1) > th > p > a
  title = song.select('p.title > a')[0].text
  # 가수 #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(8) > p > a
  singer =song.select('p.artist > a')[0].text
  #앨범 #CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(9) > a
  album =song.select('a.album')[0].text

  
  print(title, singer, album, sep=' ')
  song_data.append(['Bugs', rank, title, singer, album])
  rank += 1
  
import pandas as pd
colums =['서비스','순위','타이틀','가수','엘범']
pd_data = pd.DataFrame(song_data, columns=colums)
print(pd_data.head(10))
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)

