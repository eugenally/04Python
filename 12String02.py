'''
서식문자로 문자열 , 정수, 실수 표현
형식] "%s %d %f등이 포함됨 문자열" %값 또는 변수
'''


# 문자열 사용
srt = '내이름은  %s 입니다.' % '칸'
print("str1=", str)

# 리스트를 for 문으로 반복해서 문자열 출력
names = ['유비','관우','장비']
for n in names:
  print('이름 : %s' % n)
  
#정수사용
money = 100000
str  = '마우스의가격은 %d원입니다.' %money
print(str)

#실수사용
pi = 3.141592
print('원주율은 %f' % pi)
#소수 이하는 3자리 까지 포현
print('원주율은 %5.3f' % pi)

# 변수가 2개 이상일때
str = '이름 : %s . 나이 : %d ' % ('홍길동',99)
print(str)

# 변수 여러개를 선언및  초기화
phone, age, height = '010-1234-5678', 28, 181.5
str2 = '전화번호 : %s, 나이 : %d, 키 : %f' % (phone, age, height)
print('str2=', str2)