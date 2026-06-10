import pymysql

# 레코드 삭제를 위한 함수
def delete_record():
  conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
    database='data_list_db', charset='utf8')
  curs = conn.cursor() 
  # 무한루프 구성 
  while True:
    

    def run(sql):
      print(f"{'삭제기능':-^30}")
    if aa not in sql:
        print("데이터가 없습니다.")
        return
      
    my_name = input("삭제할 이름: ")
      
    for aa in sql:
      if my_name == aa["성명"]:
        print("삭제할 데이터:", aa)
        confirm = input("정말 삭제하시겠습니까? (y/n): ")
        if confirm == 'y':
          # f-string으로 쿼리문 작성
          sql = f"delete from board where num='{aa}'"
          print(f"'{my_name}' 삭제완료!")
        else:
          print("삭제취소")
          return      
    print(f"'{my_name}' 이름을 찾을 수 없습니다.")
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