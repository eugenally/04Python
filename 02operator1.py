#산술연산자
# 3개의 정수형변수 선언
x =2
y =4
z =8


print('x+y=',x+y)
print('x-y=',x-y)
print('x*y=',x*y)
# 나누기 연산. 결과는 (float)형으로 반환.
print('x/y=',x/y)
# 몫을 구하기 위한 나누기 연산. 결과는 정수(int)형으로 반환.
print('x//y=',x//y) #몫
print('x%y=',x%y) #나머지
# 거듭제곱. x의 y승의 결과를 반환
print('x**y=',x**y) #거듭제곱
#파이선에서 제공하는 기본함수로 거듭제곱의 결과를 반환
print("pow(x,y)=",pow(x,y)) #거듭제곱
# x의 y승의 결과를 z로 나눈 나머지가 반환됨
print("pow(x,y,z)=",pow(x,y,z)) #거듭제곱 후 나머지
# x를 y로 나눈 몫과 나머지를 tuple(튜플)
print("divmod(x,y)=",divmod(x,y)) #몫과 나머지

'''수학에 관련된 여러가지 함수를 가지고 있는  math 
모듈을 문서에 import한 후 펙토리얼 함수를 실행한다'''

import math
print("math.factorial(5)=",math.factorial(5)) #팩토리얼
