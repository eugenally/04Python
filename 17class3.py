'''
정보은닉
: 멤버변수의 외부접근을 차단하고 클래스 내부에서만 접근 하도록
설정 하는것을 말한다.
파이선에서는 private과 같은 접근 지정자 대신. 더블언더바(__)를 사용한다.
'''

class Computer:
  # 2개의 맴버변수 정의
  def __init__(self, name, passwd):
    # 외부접근이 허용되는 멤버변수(Public) 
    self.name = name
    # 외부접근이 차단된 멤버변수(Private)
    self.__passwd =passwd
  # 멤버함수
  def hitKeyboard(self):
    return f'{self.name}로 키보드 작업을 합니다.'
  def clickMouse(self):
    print(f'{self.name}에서 마우스로 클릭합니다.')
  # 정보은닉된 멤버변수의 접근의 위해 getter/setter정의
  def getPasswd(self):
    return self.__passwd
  def setPasswd(self,passwd):
    self.__passwd = passwd

# 인스턴스 생성 
myCom = Computer('LG Gram', 'qwer1234')
# 멤버함수 호출
# 외부 호출 정상출력
print("컴퓨터이름", myCom.name)

# private이므로 접근 한수 없어 에러발생
# AttributeError발생됨
# print("패스워드", myCom.__passwd)
# 접근이 안되므로getter를 통해 접근 후 출력
print('패스워드', myCom.getPasswd())


# 패스워드 변경을 위해 setter를 호출
myCom.setPasswd('abcd7890')
print('패스워드 변경후 1', myCom.getPasswd())
'''
맹글링 규칙에 의행 정보 은닉된 멤버변수는 내부적으로 이름이 변경된다.
따라서 아래와 같이 작성하면 값이 변경 되지 않는다. 또한
에로도 발생하지 않는다.
'''
myCom.__passwd = "xxxXXX"
print('패스워드 변경후 2', myCom.getPasswd())
''''
정보은닉된 멤버변수는 아래와 같이 클래스명을 포함한 형태로 이름이 
변경된다. 하지만 권장사항은 아니므로 사용하지 않는것이 좋다.
'''
# 권장되지 않음
print("맹글링 법칙", myCom._Computer__passwd)
