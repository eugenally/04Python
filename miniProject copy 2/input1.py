from db_config import get_conn



def run(data_list):
  print(f"{'입력기능':-^30}")
  name = input("성명>>>")
  tel = input("전화>>>")
  addr = input("주소>>>")
  
  dic = {"성명": name, "전화": tel, "주소": addr}
  data_list.append(dic)
  print('주소입력완료', dic)
  
  conn = get_conn()
  curs = conn.cursor()
  try:
    sql = f"INSERT INTO board (name, tel, addr) VALUES ('{name}', '{tel}', '{addr}')"
    curs.execute(sql)
    conn.commit()
    print("입력완료!")
  except Exception as e:
    conn.rollback()
    print("오류발생:", e)
  finally:
    conn.close()

