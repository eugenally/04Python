from db_config import get_conn

def run(data_list):
  
    
  print(f"{'수정기능':-^30}")
  my_name = input("수정할 이름: ")
  conn = get_conn()
  curs = conn.cursor()
     
  try:
    # 기존 데이터 확인
    curs.execute(f"SELECT * FROM board WHERE name='{my_name}'")
    row = curs.fetchone()  
    if not row:
      print(f"'{my_name}' 이름을 찾을 수 없습니다.")
      return
    print("현재 정보:", row)
    new_name = input("새 성명>>> ")
    new_tel = input("새 전화>>> ")
    new_addr = input("새 주소>>> ")
     
    sql = f"UPDATE board SET name='{new_name}', tel='{new_tel}', addr='{new_addr}' WHERE name='{my_name}'"
    curs.execute(sql)
    conn.commit()
    print("수정완료!")  
  except Exception as e:
        conn.rollback()
        print("오류발생:", e)
  finally:
    conn.close()     
        
