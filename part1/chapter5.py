
import part1.stock
# 프로그램을 시작할 때 실행된다.

import time
import random
import os

'''
Ex)
함수의 입력: 출력 횟수
함수의 출력: '대신증권'이라는 문자열(횟수만큼)
함수의 동작: 출력 횟수만큼 '대신증권' 문자열을 출력
'''
def print_ntimes(n):
    for i in range(n):
        print("대신증권")


'''
함수 호출 단계(변수 인자값 바인딩, 인자값은 메모리에 할당) 
-> 함수 실행단계(실행 중 각 변수가 바인딩하는 값이 메모리의 어딘가에 실제로 위치)
-> 함수 종료 단계(함수 내에서 생성된 모든 메모리 해제)
'''
# 어떤 주식 종목의 전날 종가를 입력받아 상한가를 계산하고 그 값을 반환
def cal_upper(price):
    increament = price * 0.3
    upper_price = price + increament
    return upper_price


def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price



def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return upper, lower


# 'tuple'이라는 하나의 객체만을 반환
upper, lower = cal_upper_lower(10000)
ret = cal_upper_lower(5000)
#print(type(ret))        # <class 'tuple'>



print(time.time())      # 1970년 1월1일 0시0분0초 기준, 초 단위
print(time.ctime())
# print(type(_))     # 파이썬 IDLE에서 가장 최근의 반환값을 바인딩하고 있는 변수: _
# print(type(time.ctime()))       # str
# 함수를 만들 때 --> 함수의 입력, 출력, 함수의 동작을 파악
cur_time = time.ctime()
print(cur_time.split(' ')[-1])

'''
for i in range(10):
    print(i)
    time.sleep(1)
'''

print(time)     # <module 'time' (built-in)>
print(random)   # <module 'random' from '/Users/kihunahn/anaconda/lib/python3.6/random.py'>

print(dir(time))

print(os.getcwd())
print(os.listdir())     # 현재 경로에 존재하는 파일과 디렉터리 목록 리스트

for x in os.listdir():
    if x.endswith('py'):
        print(x)


# 내장함수
input = [5, 2, 3, 1]
print(sorted(input))
print(min(input))
print(max(input))

for i, num in enumerate(input):
    print(i, num)
