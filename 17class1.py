'''
클래스 정의
'''

class Person:
  # private string init
  # 생성자 함수. 첩번짯매개 변수로 자신을 가르키는 self사용.
  def __init__(self, name, age):
    # 멤버변수 선언및 초기화
    self.name = name
    self.age = age
  # 멤버함수 정의
  def showInfo(self):
    # 멤버변수 출력용으로 정의
    print(f"이름 : {self.name}")
    print(f"나이 : {self.age}")
  def justDoIt(self, act):
    # 멤버변수와 매개변수를 동시에 출력하는 용도로 정릐 
    print(f"{self.name}님이 {act}를(을) 합니다.")
  '''
  Java의  toString()과 동일한 역할의 함수로 인스턴스 변술르
  그대로 출력할때 문자열로 반환 해준다.
  '''
  def __str__(self):
    return f"제 이르믄 {self.name}({self.age}) 입니다."
  
# 인스턴스 생성 -- = new -- . Java와 같이 new를 사용하지 않는다.
person1 = Person('박찬호', 30)
person2 = Person('손흥민', 28)

# 인스턴스 변수를 통해 맴버 함수 호출
person1.showInfo()
person1.justDoIt('야구')

'''
toStrint()의 역할응 하는 __str__()를 통해 반환된 문자열이
출력된다. 이 함수를 정의하지 않으면 인스턴스 참조값이 출력된다.
'''

print(person2)
person2.justDoIt('축구')
    
    