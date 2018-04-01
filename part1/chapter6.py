
from part1.ClassModule import *

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


print('\n\n')

print(Stock.__dict__)

s1 = Stock()
s2 = Stock()
print(id(s1))
print(id(s2))

print(dir())
print(s1.__dict__)
print(s2.__dict__)

s1.market = "kosdaq"
print(s1.__dict__)
print(s2.__dict__)
print(s2.market)
# 인스턴스의 네임스페이스에 해당 이름이 없으면
# 클래스의 네임스페이스로 이동



print('\n\n')

father = Parent()
father.can_sing()

child1 = LuckyChild()
child1.can_sing()

child2 = LuckyChild2()
child2.can_sing()
child2.can_dance()

'''
child3 = UnLuckyChild()
child3.can_sing()   # AttributeError: 'UnLuckyChild' object has no attribute 'can_sing'
'''


########## 연습 문제 ##########
print('\n\n')
print('6-1')
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

print('\n\n')
print('6-2')
p1 = Point(2, 3)
print(p1.x, p1.y)
p1.setx(5)
print(p1.x, p1.y)
p1.sety(7)
print(p1.x, p1.y)
p1.move(5, 3)
print(p1.x, p1.y)
p1.get()


print('\n\n')
print('6-3')
class Stock():
    market = "kospi"
a = Stock()
b = Stock()


print('\n\n')
print('6-4')
print(a.market)
print(a.__dict__)
print(b.market)
print(Stock.market)
a.market = 'kosdaq'
b.market = 'nasdaq'
print(a.market)
print(a.__dict__)
print(b.market)
print(Stock.market)


print('\n\n')
print('6-5')
