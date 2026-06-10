import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
    database='data_list_db', charset='utf8')
curs = conn.cursor() 

# SQL작업을 위해서는 반드시try~except로 예외처리 해야한다.
try:
  # 쿼리문 작성 및 실행
  sql = "SELECT * FROM board"
  curs.execute(sql)

  def run(sql):
    print(f"{'출력기능':-^30}")  
    if not sql:
      print("데이터가 없습니다.")
      return
    for i, d in enumerate(sql, 1):
          print(f"{i}. {d}")
except Exception as e:
  print('쿼리실행시 오류발생', e)
  
print('-'*40)
conn.close()
print('자원반납')