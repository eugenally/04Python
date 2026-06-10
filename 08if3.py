'''
퀴즈1] 국,영,수 점수를 입력받아 평균값을 구하고 이를 통해 학점을 출력하는 
    프로그램을 작성하시오. 
    90점 이상은 A학점 
    80점 이상은 B학점
    70점 이상은 C학점
    60점 이상은 D학점    
    60점 미만은 F학점으로 판단하여 출력합니다. 
'''
print(f"{'학점계산':-^30}")
num1 = int(input("국어점수: "))
num2 = int(input("영어점수: "))
num3 = int(input("수학점수: "))

avg = (num1+num2+num3)/3

if avg >= 90:
  print(" A학점 ")
elif avg >= 80:
  print(" B학점 ")
elif avg >= 70:
  print(" C학점 ")
elif avg >= 60:
  print(" D학점 ")
else :
  print("F")




'''
퀴즈2] 아이디를 먼저 입력받은 후 user_info 리스트에 등록되었다면 패스워드를 입력받아 일치하는지 확인하는 프로그램을 작성하시오. 여기서 패스워드는 1234로 가정합니다. 
'''

print(f"{'Login':-^30}")




user_info = ['sung', 'kim', 'hong', 'park', 'lee']

id = input("ID: ")


if id in user_info :
  print("{}의 비밀번호를 입력하세요.".format(id))
  
  pass_info = ['123']
  password = input("PASSWORD: ")
  if password in pass_info :
    print("로그인 성공")
  else :
    print("비밀번호가 다릅니다.")
  
else :
  print("{}Signin 하세요.".format(id))



# 강사님 답안
user_info = ['sung', 'kim', 'hong', 'park', 'lee']

match_flag = False # 표시를 위한 메시지

my_id = input('아이디를 입력하세요:')
for aa in user_info:
    if my_id == aa:
        match_flag = True # 표시를 위한 메시지
        my_pass = input('패스워드를 입력하세요:')
        if my_pass == '1234':
            print('아이디와 패스워드 일치')
        else:
            print('패스워드 틀림')
if match_flag == False:
    print('일치하는 아이디가 없습니다.')
