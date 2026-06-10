
'''
map(): 주어진 함수와 컬랙션을 인수로 받아, 컬랙션의 각 요소에
함수를 적용한 결과를 반환한다. for문과 같은 반복문을 사용하지 않아도
지정한 함수로 인자를 순차적으로 전달하여 그 결과를 list로 반환한다.
'''

# 1.map()
# 함수 정의 :매개변수에 2를 곱한결과를 반환
def multiply_by_two(n):
  return n*2
#리스트 정의
numbers = [1,2,3,4,5]
# map(함수, 리스트) 와 같이 호출
result = map(multiply_by_two, numbers)
# 결과1: map object로 출력됨
print('결과 1-1', result) 
# 결과2: object를 List로 변환 후 출력
print('결과 1-2', list(result))

'''
filter(): 주어진 요소중 조건에 맞는 것만 필터링 하여 반환한다.
      즉 지정된 함수(혹은 람다식)에서 True 가 된느것만 반환하여 결과값을 반환한다.
'''

# 2.filter 함수
# 인수가 짝수일때만 True를 반환하는 함수 정의
def is_even(x):
  return x % 2 == 0 #boolean 트루값만 반환
numbers = [1,2,3,4,5]
result = filter(is_even, numbers)
# 짝수만 리스트에 남고 홀수는 필터링되어 모두 제거된 상태로 출력된,,,,
print('결과 2', result) 

'''
reduce함수 : 반복가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
    이전 결과화 누적해서 반환하는 함수. 즉 하나의 결과값을 반환한다.
    내장함수가 아니므로 임포드 한후 사용해야한다.
'''

# 3.reduce함수
from functools import reduce

def add(x,y):
  return x+y
numbers = [1,2,3,4,5]
'''
reduce함수는 처음 2개의 인수를 먼저 함수로 전달하여 결과를 만들고
그 결과를 다음 요소와 결합하는 방식으로 전체 리스트를 처리 한다.
reduce에서 사용하는 함수는 2개의 인수만 받을 수 있으므로 
매개변수를 3개 선언하면 에러가 발생한다.
'''

result = reduce(add, numbers)
print(result) 