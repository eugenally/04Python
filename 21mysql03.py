import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
    database='sample_db', charset='utf8')
curs = conn.cursor()

# format ()함수는 인덱스를 통해 값을 설정 할 수 있다.
sql = """update board
            set title ='{1}', content ='{2}'
            where num={0}""".format(input('수정할 일련번호:'), input('제목'), input('내용'))
            
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