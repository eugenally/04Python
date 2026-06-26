
# 판다스 뷰티풀숩, 셀레니움 모듈 임포트
from turtle import title
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# 크롬 웹 드라이버 로드 및 페이지 접속
driver = webdriver.Chrome()

url = 'https://www.genie.co.kr/chart/top200'
driver.get(url)
# 데이터 생성을 위한 리스트 생성
song_data = []
rank = 1
# 1~4페이지 까지 반복
for page in range(1,5):
  # 페이지 정보 출력및 2초간 묵시적 대기
  print("페이지", page)
  driver.implicitly_wait(2)
  
  # 파싱을 위해 페이지 소스를 얻어온 후 Soup 객체로 변환
  html = driver.page_source
  soup = BeautifulSoup(html,'html.parser')
  
  # 각 페이지의 챠트 테이블의 <tr> 부분을 선택 한 후 반복
  songs = soup.select('tbody > tr')
  for song in songs:
    # 노래제목
    # #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    title = song.select('a.title')[0].text.strip()
    # #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
    singer = song('a.artist')[0].text
    song_data.append(['Ginie',rank ,title, singer])
    rank += 1
    ''''
    페이지 하단의 다음 페이지로 가기위한 버튼을 클릭한다.
    각 버튼의 XPath 패턴은 a[1]~a[4]와 같이 되어있다
    '''
  if page<4:
    driver.find_element(
      By.XPATH,
      f'//*[@id="body-content"]/div[7]/a[{page+1}]'
    ).click()
  # 다음페이지로 넘어가고 5초간 묵시적 대기
  driver.implicitly_wait(5)

# 리스트를 데이터 프레임으로 변환 및 컬럼 추가 
colums =['서비스','순위','타이틀','가수']
pd_data = pd.DataFrame(song_data, columns=colums)
# 데이터 프레임의 최상의 5개 데이터 확인
print(pd_data.head(10))
# 엑셀저장
pd_data.to_excel('./saveFiles/genie_chart.xlsx', index=False) 

