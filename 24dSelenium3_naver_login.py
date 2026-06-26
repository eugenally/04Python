# 셀레니움 모듈과 드라이버를 로드한다

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 로드
driver = webdriver.Chrome()

# 네이버 메인에 접속한 후 페이지의 정보 얻어옴
url = 'https://www.naver.com/'
driver.get(url)

# XPath로 이용해서 네이버 메인의 '로그인' 버튼을 찾은 후 클릭
driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click()
# 페이지 로딩과 상관없이 무조건 2초대기
time.sleep(2)
# 로그인 페이지로 이동 후 아이디/비번 입력상자를 찾은 후 정보 입력
# 이때는 <input>태그의 name속성을 통해 엘리먼트 선택
driver.find_element(By.NAME, 'id').send_keys('eugenally')
time.sleep(2)
driver.find_element(By.NAME, 'pw').send_keys('Eugemagg09!^')
time.sleep(2)
# 입력이 완료되면 ' 로그인' 버튼을 클릭해서 로그인 시도
driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
# 대부분 포털 사이트에서 셀레니움 로그인을 감지하여 '캡챠'화면으로 이동함
time.sleep(100)
# 조금 긴 시산을 대기 하면서 직접 입력해 준다.
# 로그인이 완료되면 메인으로 자동 이동 하므로, 상단 검색창에 검색어 입력
driver.find_element(By.NAME, 'query').send_keys('가산디지털 맛집')
time.sleep(2)

# '검색'버튼을 눌러 결과 확인
driver.find_element(By.CLASS_NAME, 'btn_search').click()
time.sleep(10)


'''
24dSelenium3_naver_login.py

Xpath
//*[@id="account"]/div/a
'''
