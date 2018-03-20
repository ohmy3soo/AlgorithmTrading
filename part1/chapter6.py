from part1.ClassModule import BusinessCard
from part1.ClassModule import Myclass

member1 = BusinessCard()
print(member1)
print(type(member1))

member1.set_info("Yuna kim", "yunakim@naver.com", "Seoul")
# self.변수명 --> 인스턴스 변수
# 클래스를 정의하는 순간에는 생성할 인스턴스의 이름을 모르기 때문에 self를 사용한다.
print(member1.name)
print(member1.email)
print(member1.addr)


member2 = BusinessCard()
member2.set_info("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")
print(member2.name)
print(member2.email)
print(member2.addr)

member1.print_info()


#inst1 = Myclass()
inst1 = Myclass("Kangsan Lee", "kangsan.lee", "USA")
inst1.print_info()