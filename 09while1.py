'''
반복문 : 파이썬에서의 반복문은 While과 for만 있다.
형식]
      초깃값
      While 조건문:
        실행 문장
        등감식
      else:
        정상종료되었을때 실행됨
파이선에서는 반복문도 Else구문을 사용할 수있다.
단 while문이 완료되지 않은 상태로 탈출 하면 else구문은 실행되지 않는다.
'''



'''
시나리오] 열번찍어 안넘어 가는 나무없다는 속담을 while 문으로 구현하시오
'''



treeHit = 0
while treeHit <10:
  treeHit = treeHit + 1
  # %를 이용해서 문자열과 연결하면 Printf()와 유사하게 사용 가능
  print("나무를 %d번 찍었습니다." % treeHit) # 나무를 9번 찍었습니다. % 가 대입됨
  if treeHit == 10:
    print("나무가 넘어갑니다.")
    
print()
print("="*30) 


# 파이선에서는 문자열을 조건식으로 사용할 수있다.
str = 'python'
# str이 빈문자열이 될때까지 반복한다.
while str :
  # 출력문 끝에 공백을 추가하여 줄바꿈 없이 출력
  print(str, end =' ')
  # 인덱스 1부터 끝까지 슬라이싱, 즉 첫글자를 제거한 후 대입
  str = str[1:]
  
print()
print("="*30) 

#시나리오 1~10까지의 합을 구하시오

sum = 0
i = 1
while i<=10:
  # 증가하는 i를 누적해서 더함 
  sum += i
  if i<10:
    # 반복중에는 줄바꿈 없이  +기호 출력
    print(i, end=" + ")
  else:
    # 반복의 마지막에는 =을 출력
    
    print(i, end=" = ")  
  i += 1
else:
  # while문이 종료되면 else구문이 실해되어 합의 결과 출력
  print(sum)
  
print()
print("="*30) 

''''
시나리오] 하루에 팔수있는 커피는 모두 10잔이다.
while문으로 무한루프를 만든 후 10잔의 커피가 모두 판매되었을때 
반복문을 탈출하는 프로그램을 작성하시오 단, break를 사요하시오
'''

coffee = 10
# 조건을 True로 지정하여 무한루프 구성
while True:
  print("커피한잔을 판매합니다.")
  coffee = coffee -1
  print("남은 커피의 양은%d개 입니다." % coffee)
  # 커파가 0이 되면 break를 통해  while문 탈출
  if coffee ==0:
    print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
    break
  
print()
print("="*30) 

''''
시나리오] 로또번호를 생성하는 프로그램을 작성하시오.
1~45 사이에서 중복되지 않는 숫자 6개를 추출하면 된다.
'''


# random모듈  임포트
import random
# 새로운set생성
lotto = set()
# 무한루프 조건으로 while 문 정의
while True:
  #1~45까지의 난수 생성
  rndNum = random.randint(1,45)
  #생성된 난수를 set에 추가. 이때 중복은 자동으로 제거됨.
  lotto.add(rndNum)
  #set의 크기, 즉 6개의 요소가 채워졌다면 while문 탈출
  if len(lotto) == 6:
    break
# 오름차순 sorted정렬 후 출력,,reverse=True 옵션으로 내림차순도 가능함
#print("로또번호:", sorted(lotto,reverse=True))
print("로또번호:", sorted(lotto))
 
