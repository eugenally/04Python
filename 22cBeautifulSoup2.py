
import requests
from bs4 import BeautifulSoup

# KBO타자 기록실
response = requests.get('https://www.koreabaseball.com/Record/Player/HitterBasic/BasicOld.aspx?sort=HRA_RT')
# HTML 소스저장(택스트 형식)
html = response.text
# 파싱을 위해  Soup 객체로 변환
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

# 타이틀 파싱 : 선수기록(HTML태그 포함)
title = soup.select_one('#cphContents_cphContents_cphContents_udpContent > h4')
#print('title요쇼 :', title)

# 테그르 제거한 후 순수한 택스트만 추출
title_txt = title.get_text()
#print('title 텍스트 :', title_txt)

# 타자기록이 있는 <table> 태그 전체 얻어오기
record_table = soup.select_one('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')
#print('타자기록요소 :', record_table)


# 타자 기록이 반복출력되는 <tbody>를 얻어온 후 <tr>의 갯수만큼 반복
record_tr = soup.select_one('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody')
# select()함수는 반복되는 요소를 List로 얻어온다.
repeat_tr = record_tr.select('tr')
for rec in repeat_tr:
  #print('dddd', rec)

  d1 = rec.select_one('td:nth-child(1)').get_text().strip()   # 순위
  d2 = rec.select_one('td:nth-child(2)').get_text().strip()   # 선수명
  d3 = rec.select_one('td:nth-child(3)').get_text().strip()   # 팀명
  d4 = rec.select_one('td:nth-child(4)').get_text().strip()   # AVG (타율)
  d5 = rec.select_one('td:nth-child(5)').get_text().strip()   # G (경기수)
  d6 = rec.select_one('td:nth-child(6)').get_text().strip()   # PA (타석)
  d7 = rec.select_one('td:nth-child(7)').get_text().strip()   # AB (타수)
  d8 = rec.select_one('td:nth-child(8)').get_text().strip()   # H (안타)
  d9 = rec.select_one('td:nth-child(9)').get_text().strip()   # 2B (2루타)
  d10 = rec.select_one('td:nth-child(10)').get_text().strip() # 3B (3루타)
  d11 = rec.select_one('td:nth-child(11)').get_text().strip() # HR (홈런)
  d12 = rec.select_one('td:nth-child(12)').get_text().strip() # RBI (타점)
  d13 = rec.select_one('td:nth-child(13)').get_text().strip() # SB (도루)
  d14 = rec.select_one('td:nth-child(14)').get_text().strip() # CS (도루실패)
  d15 = rec.select_one('td:nth-child(15)').get_text().strip() # BB (볼넷)
  d16 = rec.select_one('td:nth-child(16)').get_text().strip() # HBP (사구)
  d17 = rec.select_one('td:nth-child(17)').get_text().strip() # SO (삼진)
  d18 = rec.select_one('td:nth-child(18)').get_text().strip() # GDP (병살타)
  d19 = rec.select_one('td:nth-child(19)').get_text().strip() # E (실책)
    
  # 출력 확인용
  #print(f"{d1}위 - {d3} {d2} (타율: {d4}, 홈런: {d11})")
  print(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19)

'''
#cphContents_cphContents_cphContents_udpContent > div.record_result > table
#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody

'''
