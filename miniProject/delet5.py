def run(data_list):
  print(f"{'삭제기능':-^30}")
  if not data_list:
      print("데이터가 없습니다.")
      return
    
  my_name = input("삭제할 이름: ")
    
  for aa in data_list:
    if my_name == aa["성명"]:
      print("삭제할 데이터:", aa)
      confirm = input("정말 삭제하시겠습니까? (y/n): ")
      if confirm == 'y':
        data_list.remove(aa)
        print(f"'{my_name}' 삭제완료!")
      else:
         print("삭제취소")
         return      
  print(f"'{my_name}' 이름을 찾을 수 없습니다.")