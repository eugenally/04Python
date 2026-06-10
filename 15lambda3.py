

# 람다식과 map, filter, reduce 함수활용
print(f"{'람다식과 map함수1':-^30}")
# 매개변수에 2를 곱한 결과를 반환하는 람다식 정의
multiLambda = lambda x: x*2
list_data = [1,2,3,4,-1,-2,-5,-10]
#리스트의 크기만큼 람다식을 호출해서 반환된 결과를 리스트로 변환후 변수에 저장한다.
result = list(map(multiLambda, list_data))
# 각 요소에 2ㄹ르 곱한 결과를 담은 리스트가 출력된다.
print('결과1',result)
'''
람다식에서 삼항 연산자(조건부 표현식)사용하기
형식] 식1 if조건식 else 식2
    -조건식이 True 일때 식1 false 일때 식2를 선택
    -ifㄹ를 사용햇다면 반드시 else를 사용해야함
    -elif는 사용할 수 없음
'''

print(f"{'람다식과 map함수2':-^30}")
list_data2 = [1,2,3,4,5,6,7,8,9,10]
# 인수가 3의 배수이면 'x3'을 반환하고, 아니면 정수를 그대로 반환
strNumLambda = lambda x: '3x' if x%3==0 else x
result = list(map(strNumLambda, list_data2))
# 3의 배수는 문자열로, 나머지는 정수 그대로 출력된다.
print('결과2',result)

print(f"{'람다식과 filter함수':-^30}")
list_data3 = [1,2,9,16,25,46,64,81,100]
# 5초과 80미만 요소일때만 반환하도록 람다식 저의함
result = list(filter(lambda z: z>5 and z<80, list_data3))
# 9~64까지의 요소만 리스트에 남는다. 즉 그위는 필터링된다.
print('결과3',result)



print(f"{'람다식과 reduce함수':-^30}")
import functools, operator
# 2개의 요소를 더한 결과를 반환하는 람다식 정의
sum1 = functools.reduce(lambda i, j: i + j, range(1,11))
'''
range(1,11)-> [1,2,3,4,....,10]을 생성함
1회차 : 1,2가 매개변수로 전달되어 결과3이 반환됨
2회차 : 1회차의 결과가 첫번째값, 두번째 값은 리스트의 3이 전달됨
    따라서 3+3의 결과 6을 반환한다.
3회차 : 이전결과 6, 해당회차 4를 합산하여 10이 반환된다.
따라서 1~10까지 합의 결과를 최종적으로 반환한다.
'''
print('결과4-1', sum1)

# operator모툴에서 제공한 add함수로 앞과 동일한 결과를 출력
sum2 = functools.reduce(operator.add, range(1,11))
print('결과4-2', sum2)