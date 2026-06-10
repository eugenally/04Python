def run(data_list):
    if not data_list:
      print(f"{'수정기능':-^30}")
      print("데이터가 없습니다.")
      return
    
    my_name = input("수정할 이름: ")
    
    for aa in data_list:
      if my_name == aa["성명"]:
        print("현재 정보:", aa)
        aa["성명"] = input("새 성명>>> ")
        aa["전화"] = input("새 전화>>> ")
        aa["주소"] = input("새 주소>>> ")
        print("수정완료!", aa)
        return
    
    print(f"'{my_name}' 이름을 찾을 수 없습니다.")