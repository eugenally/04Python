import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
    database='data_list_db', charset='utf8')
curs = conn.cursor() 
# f-string을 통해 문자열 중간에 {}로 input()함수 호출 문장 삽입
sql = f"""INSERT INTO board (name, tel, addr) VALUES (
  '{input('성명')}','{input('전화')}','{input('주소')}')"""

try:

  print(f"{'입력기능':-^30}")

  def run(data_list):
    print(f"{'입력기능':-^30}")
    name = input("성명>>>")
    tel = input("전화>>>")
    addr = input("주소>>>")
  
    dic = {"성명": name, "전화": tel, "주소": addr}
    data_list.append(dic)
    print('주소입력완료', dic)
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