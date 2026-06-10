

import input1
import output2
import search3
import correct4
import delet5

data_list = [] 

def menu():
  print('메뉴중 숫자를 선택하세요:')
  print('1.입력 2.출력 3.검색 4.수정 5.삭제')
  print('6.종료')
  # 입력 받은 문자를 반환한다.
  return input('번호선택:')

while True:
  #함수의 반환값을 정수로 변환 후 변수에 저장
  choice = int(menu())
  if choice ==1:
    input1.run(data_list)
    
  elif choice ==2:
    output2.run(data_list)
    
  elif choice ==3:
    search3.run(data_list)
    
  elif choice ==4:
    correct4.run(data_list)
    
  elif choice ==5:
    delet5.run(data_list)
    
  elif choice ==6:
    break
print(f"{'종료합니다.':-^20}")
    

    
   
  






