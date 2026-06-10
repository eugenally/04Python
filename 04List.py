
'''
리스트(list)
:대괄호[] 안에 콤마로 항목를 구분하여, 대입 연산자로 항목을 변경
할수 있는 시퀀스 자료형이다. 서로 다른 자료형의 항목르오
구성할 수 있고 인덱싱, 슬라이싱, 연결, 반복, 등잉 가능하다.
'''
# random모듈을 통해 6~10 사이의 난수 생성
import random
rndNum = random.randint(6,10)

#선언
# 정수로 선언된 리스트
list1 = [1,2,3,4,5,rndNum]
# 문자로 구성된 리스트
list2 = ['Java','HTML','Python']
# 중첩된 구조의 리스트
list3 = [10, 20,['Java','HTML','Python']]

#출력
# 리스트 명을 사용하면 전체 항목이 출력됨
print('list1', list1)
# 인덱스를 통해 출력가능
print('list2[2]', list2[2])
print('list3[2]', list3[2])

#슬라이싱
print(f"{'슬라이싱':-^30}")
print('list1[1:4]', list1[1:4]) # 인텍스 1~3까지 출력
print('list2[2]', list1[:3]) # 시작을 생략하면 0부터
print('list1[1:]', list1[1:]) # 종료가 없으면 끝까지

print(f"{'리스트 연결':-^30}")
# 리스트간 연결을 하면 중첩된 리스트 형태로 삽입된다.
all_list = [list1, list2]
print('all_list',all_list)
print('all_list[1][0]',all_list[1][0])#'Java'출력됨 2번째 리스트의 1번째 

#list 관련 메소드
print(f"{'list관련 메소드':-^30}")
# 11~20 사이의 난수생성
rndNum = random.randint(11,20)

# 리스트의 마지막 부분에 항목추가
list1.append(rndNum)
print(f'append({rndNum})', list1)

#전체항목 삭제
list1.clear()
print('clear()', list1)

# 리스트 확장
list1.extend([10,20,30,40,50])
print('extend()', list1)

#지정된 인덱스에 요소 삽입
list1.insert(1,99)#1번 인덱스에 99삽입
print('insert()', list1)

# 리스트의 마지막 항목 삭제 및 반환. 즉 삭제와 동시에 출력 할 수있음
print(list1.pop())
print('pop()', list1)

# 항목을 지정해서 삭제
list1.remove(99)
print('remove()', list1)

# 리스트를 뒤집을 때 사용
list1.reverse()
print('revers()', list1)

# 지정한 인덱스의 요소를 del 키워드를 통해 삭제
del list1[0]
print('0번 삭제후', list1)