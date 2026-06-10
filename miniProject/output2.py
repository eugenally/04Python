def run(data_list):
  print(f"{'출력기능':-^30}")  
  if not data_list:
      print("데이터가 없습니다.")
      return
  for i, d in enumerate(data_list, 1):
      print(f"{i}. {d}")