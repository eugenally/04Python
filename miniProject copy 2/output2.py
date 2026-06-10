from db_config import get_conn

def run(data_list):
    print(f"{'출력기능':-^30}")
    conn = get_conn()
    curs = conn.cursor()
    try:
        curs.execute("SELECT * FROM board")
        rows = curs.fetchall()
        if not rows:
            print("데이터가 없습니다.")
            return
        for row in rows:
            print(row)
    except Exception as e:
        print("오류발생:", e)
    finally:
        conn.close()