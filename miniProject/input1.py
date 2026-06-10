print(f"{'입력기능':-^30}")

def run(data_list):
  print(f"{'입력기능':-^30}")
  name = input("성명>>>")
  tel = input("전화>>>")
  addr = input("주소>>>")
  
  dic = {"성명": name, "전화": tel, "주소": addr}
  data_list.append(dic)
  print('주소입력완료', dic)

