'''
내장함수(Built in Function)
  :내장함수는 외부모듈과 달리 import가 필요하지 않으므로 별도의설정 없이
  바로 사욯할수있다  
'''

print(f"{'기본 내장함수':-^30}")
# renge()함수를 통해 1~10까지 생성하여 list로정릐
data1 = list(range(1,11)) 
print(data1)
# 내장함수를 통해 크기, 합계 등을 확인 할 수있다.
print('len=', len(data1))
print('sum=', sum(data1))
print('max=', max(data1))
print('min=', min(data1))

'''
순서가 있는 자료형(리스트 ,튜플, 문자열 등)을 전달 
받아 인덱스를 포함하는 값을 반환한다.
'''

print(f"{'enumerate()':-^30}")
# 인덱스(0,1,2,)와 값을 함께 반환하여 출력한다.
for i, k in enumerate(data1):
  
  print(i, k, end=', ')
print()

# 딕셔너리 생성,
data2 = dict(birth=1970, name='홍길동', size='100츠')
# 딕셔너리 생성을 통해 반복하면 Index와 Key를 반환한다..
for i, k in enumerate(data2):
  # i는 인덱스(0,1,2...), k는 딕셔너리의 key가 반환됨.
  # 반환된 key를 통해 Valueㄹ르 인출할 수있다.
  print(i, k, data2[k], end=', ')
print()


# 실행 가능한 문자열을 전달 받아 결괏값을 반환한다.
print(f"{'eval()':-^30}")
print(eval('1+2'))
print(eval("'hi'+'a'"))

# 입력값응 정렬 한되 리스트로 반환
print(f"{'sorted()':-^30}")
numbers = (8,7,6,8,4,9,7,5,3,2,7,4,9,8,2,6,5)
print(sorted(numbers))

'''
값을 차례대소 꺼낼 수있는 객체 
for i in range(100):과 같이 작성하면 파이선은 0~99까지
값을 차례대로 꺼낼수 있는 이터레이터를 생성 하여 숫자를 생산한다.

iter() : 반복을 끝낼 값(Sentinel)을 지정하면 특정 값이 나올때
반복를 종료하는 함수
형식]
    iter(반복가능한 객체, 반복을 끝낼값)
'''

print(f"{'이터레이터(iterator)':-^30}")
it = iter([1,2,3,4,5,99])
while it:
  row = next(it)
  # 조건문을 통해 99가 되면 while문을 탈출
  if row == 99:
    break
  print(row, end=", ")
print()

# 난수생성을 위한 모듈 임포트
import random
count = 0
# iter()함수를 통해 반복. 2가나오면 반복이 종료된다.
for i in iter(lambda : random.randint(0,10),2):
  print(i, end=', ')
  count += 1
else:
  print('\n난수 2 가 생성되어 종료')
print(f"{'반복횟수:{count}'}")