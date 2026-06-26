
import pandas as pd

# 데이터를 딕셔너리로 정의
data1 = {
  '이름' : ['공민철', '강백호', '서태웅', '채치수', '송태섭'],
  '국어' : [ 100, 80, 90, 84, 200],
  '여어' : [ 100, 80, 90, 84, 200],
  '수학' : [ 100, 80, 90, 84, 200],

}
data2 = {
  '이름' : ['알리스', '밥', '찰리', '데이비드', '아부'],
  '나이' : [ 100, 80, 90, 84, 200],
  '취미' : [ '독서', '피아노', '그밍', '기타', '짹스'],
  '특기' : [ '피아노', '마라톤', '프로그래믿', '등산', '잠수'], 
  '생년월일' : ['1990-03-15', '1985-07-22', '1992-11-08', '1998-01-30', '1995-06-14'],
  
}

#딕셔너리를 데이터 프레임으로 변환 후 첫번째 컬럼인 "이름"을 인덱스로 저장

df1 = pd.DataFrame(data1)
df1.set_index('이름',inplace=True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('이름', inplace=True)
print(df2)

# 각 데이터프레임을 지정한 sheet에 저장
writer = pd.ExcelWriter("./saveFiles/sheetGubun.xlsx")
df1.to_excel(writer,sheet_name='sheei1')
df2.to_excel(writer,sheet_name='sheet2')
# sheet를 지정한 이후 저장시에는 _save()함수를 추가로 실행 한다
writer._save()