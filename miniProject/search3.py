def run(data_list):
    if not data_list:
        print("데이터가 없습니다.")
        return
    
    my_name = input("검색할 이름: ")
    result = []
    
    for aa in data_list:
        if my_name == aa["성명"]:
            result.append(aa)
    
    if result:
        print(f"--- 검색결과 {len(result)}건 ---")
        for r in result:
            print(r)
    else:
        print(f"'{my_name}' 이름을 찾을 수 없습니다.") 
  
  