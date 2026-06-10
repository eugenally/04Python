import pymysql

conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
    database='data_list_db', charset='utf8')
curs = conn.cursor() 


# SQL작업을 위해서는 반드시try~except로 예외처리 해야한다.
try:
  # 쿼리문 작성 및 실행
  sql = "SELECT * FROM board"
  curs.execute(sql)

  def run(data_list):
    if not data_list:
      print(f"{'수정기능':-^30}")
      print("데이터가 없습니다.")
      return
    
    my_name = input("수정할 이름: ")
    
    for aa in data_list:
      if my_name == aa["성명"]:
        print("현재 정보:", aa)
        aa["성명"] = input("새 성명>>> ")
        aa["전화"] = input("새 전화>>> ")
        aa["주소"] = input("새 주소>>> ")
        print("수정완료!", aa)
        return
    
    print(f"'{my_name}' 이름을 찾을 수 없습니다.")
except Exception as e:
  print('쿼리실행시 오류발생', e)
  
print('-'*40)
conn.close()
print('자원반납')  
      