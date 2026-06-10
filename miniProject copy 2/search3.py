from db_config import get_conn

def run(data_list):
  print(f"{'검색기능':-^30}")
  my_name = input("검색할 이름: ")
  conn = get_conn()
  curs = conn.cursor()
  try:
    sql = f"SELECT * FROM board WHERE name='{my_name}'"
    curs.execute(sql)
    rows = curs.fetchall()
    if not rows:
      print(f"'{my_name}' 이름을 찾을 수 없습니다.")
      return
    print(f"--- 검색결과 {len(rows)}건 ---")
    for row in rows:
      print(row)
  except Exception as e:
    print("오류발생:", e)
  finally:
    conn.close()