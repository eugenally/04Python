'''
시나리오] 원의 넓이와 둘레를 계산할 수 있는 클래스를 작성한 후 
주어진 코드가 실행될 수 있도록 구현하시오.
circle1 = Circle(5)
print("원의넓이:", circle1.calArea())
print("원의둘레:", circle1.calRound())
'''

# 수학관련 기능을 제공하는 math모듈 임포트
import math

# 클래스 정의
class Circle:
  # 생성자
  def __init__(self, radius):
    # 맴버변수 : 반지름
    self.redius = redius
  # 멤버함수 : 넓이 계산후 결과 반환
  def calArea(self):
    return math.pi * (self.redius ** 2)
  
  # 둘레
  def calRound(self):
    return 2 * math.pi * self.redius
  # toString()과 동일한 역할의 함수 .객체 정보를 반환.
  def __str__(self) -> str:
    return f'원의 반지름은 {self.redius}입니다.'


# 반지름이 5인 원 인스턴스 생성 
circle1 = Circle(5)
# 원의 정보 출력(print() 내부에서 __str__()호출)
print(circle1)
# 멤버함수 호출후 결과 출력
print("원의 넓이: ", circle1.calArea())
print("원의 둘레: ", circle1.calRound())