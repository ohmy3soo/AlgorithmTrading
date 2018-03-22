
class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr


    def print_info(self):
        print("---------------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("---------------------------")


class Myclass:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr


    def print_info(self):
        print("---------------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("---------------------------")



# 인스턴스.method()시, 첫번째 인자(self)로 해당 인스턴스의 주소를 넘겨준다.
# 따라서 Foo.func1()은 가능하다.(인터프리터에서)
# Foo.func2()는 self값이 없으므로 오류가 발생한다.

class Foo:
    '''
        def func1():
            print("function 1")
        '''
    def func2(self):
        print("function 2")



class Stock:
    market = "kospi"



class Account:
    num_accounts = 0

    def __init__(self, name):
        self.name = name
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    # self.~ ==> 인스턴스 변수 --> 인스턴스의 네임스페이스에 위치
    # num_accounts ==> 클래스 변수 --> Account 클래스의 네임스페이스에 위치

    # 여러 인스턴스 간에 서로 공유해야 하는 값은 클래스 변수를 통해 바인딩해야 한다.
    # 파이썬은 인스턴스의 네임스페이스에 없는 이름은 클래스의 네임스페이스에서 찾아보기 때문.


class Parent:
    def can_sing(self):
        print("Sing a song")


class LuckyChild(Parent):
    pass


class LuckyChild2(Parent):
    def can_dance(self):
        print("Shuffle Dance")


class UnLuckyChild:
    pass