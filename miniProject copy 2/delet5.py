from db_config import get_conn

def run(data_list):
  print(f"{'삭제기능':-^30}")
  my_name = input("삭제할 이름: ")
  conn = get_conn()
  curs = conn.cursor()
    
  try:
    curs.execute(f"SELECT * FROM board WHERE name='{my_name}'")
    row = curs.fetchone()

    if not row:
      print(f"'{my_name}' 이름을 찾을 수 없습니다.")
      return
 
    print("삭제할 데이터:", row)
    confirm = input("정말 삭제하시겠습니까? (y/n): ")
    if confirm == 'y':
      curs.execute(f"DELETE FROM board WHERE name='{my_name}'")
      conn.commit()
      print(f"'{my_name}' 삭제완료!")
    else:
      print("삭제취소")
             
  except Exception as e:
        conn.rollback()
        print("오류발생:", e)
  finally:
        conn.close()