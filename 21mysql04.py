import pymysql
# 레코드 삭제를 위한 함수
def delete_record():
  conn = pymysql.connect(host='localhost', 
                         user='sample_user', 
                         password='1234',
                         database='sample_db',
                         charset='utf8')
  curs = conn.cursor() 
  # 무한루프 구성 
  while True:
    iStr =input('삭제할 일련번호(종료하려면 Exit):')
    # 대문자를 입력하더라도 하나의 조건으로 판단하기 위해 소문자로 변경 후 확인 한다.
    if iStr.lower() =='exit':
      print('프로그램을 종료합니다.')
      # 무한루프 탈출
      break
    # f-string으로 쿼리문 작성
    sql = f"delete from board where num='{iStr}'"
    
    try:
     # 쿼리문 실행
      curs.execute(sql)
      # 새로운 레코드가 입력되었으므로 commit( )함수 실행
      conn.commit()
  
      print("1개의 레코드가 입력됨")
    except Exception as e:
       # 오류가 발생되면 롤백처리
       conn.rollback()
       print("쿼리실행시 오류발생", e)
  # 모든 작업이 완료되면 자원해제
  conn.close()

# 함수 호출후 delete 쿼리문 실행2

delete_record()

# 결과는 num 을 포함 라인 사라짐, 13을(없는 데이터) 누르면 사라졋는지 확인 불가