'''
파이선에서 MySQL(MarinaDB)를 연동 하려면 PyMySQL을 면저 설치해하
한다
c:\> pip3 install pymysql
'''
# 모듈 임포트
import pymysql

# DB연결(호스트, DB명, 사용자계정, 패스워드 등이 필요함)
conn = pymysql.connect(host='localhost', user='sample_user', password='1234',
    db='sample_db', charset='utf8', port=3306,)

'''
port의 경우 기본포트인 3306을 사용중이라면 생략 할 수있다.만약 포트가
다른경우는 반드시 표기 해야한다.

cursorclass=pymysql.cursors.DictCursor
    이옵션을 사용하면 레코드 인출시 딕셔너리로 출력된다.
    생략시 디폴트 값은 튜플로 설정 되어있다.
'''
# 커서 생성
curs = conn.cursor() 


# SQL작업을 위해서는 반드시try~except로 예외처리 해야한다.
try:
  # 쿼리문 작성 및 실행
  sql = "SELECT * FROM board"
  curs.execute(sql)
  
  # select한 모든레코드 인출 (튜플의 형태로 인출됨) 결과만 보는용 html이나 다른작업에 불편
  rows = curs.fetchall()
  print('단순인출', rows)
  
  print(f"{'인출1':-^30}")
  # 행 단위로 하나씩 선택하여 인출
  for row in rows:
    print(row)
    print(row)
  
  print(f"{'인출2':-^30}")
  # 행단위로 인출하되 각 컬럼의 인덱스를 지정하여 개별 인출 
  for row in rows:
    # 인덱스 0은 num.이후는 순서대로 지정된다.
    # cursorclass=pymysql.cursors.DictCursor (딕셔너리 형식) row[0]=> row['num']등으로 수정 필요
    print(row[0], row[1], row[2],end= ' ')
    pdate = row[3]
    id = row[4]
    vcnt = row[5]
    # 변수에 저장한 후 서식문자를 이용해 출력
    print("%s, %s, %s" %(pdate, id, vcnt))
  
  print(f"{'인출3':-^30}")
  # 검색어와 like를 이용해서 검갯결과 인출
  sql = sql + "WHERE title like '%{0}%' ".format(input('검색어입력:'))
  curs.execute(sql)
  rows =curs.fetchall()
  print(rows)
  
except Exception as e:
  print('쿼리실행시 오류발생', e)
  
print('-'*40)
conn.close()
print('자원반납')