
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
input_list = [5, 2, 3, 1]
print(sorted(input_list))
print(min(input_list))
print(max(input_list))

for i, num in enumerate(input_list):
    print(i, num)




########## 연습 문제 ##########
print('\n\n')
print('5-1')
def myaverage(a, b):
    return (a+b)/2
print("A: 5, B: 12")
print(myaverage(5, 12))


print('\n\n')
print('5-2')
def get_max_min(data_list):
    return max(data_list), min(data_list)

data_list = [4, 2, 1, 8, 6, 5, 4, 3 ,2, 9, 0]
print("DATA_LIST: [4, 2, 1, 8, 6, 5, 4, 3 ,2, 9, 0]")
print(get_max_min(data_list))


print('\n\n')
print('5-3')
def get_txt_list(path):
    txtList = []
    fileList = os.listdir(path)
    for file in fileList:
        if file.endswith('.txt'):
            txtList.append(file)
    return txtList

print(get_txt_list(os.getcwd()))

print('\n\n')
print('5-4')
def getBMI(kg, cm):
    kg = float(kg)
    cm = float(cm)

    m = cm/100

    BMI = kg / (m**2)
    print("BMI:", BMI)
    if BMI < 18.5:
        print('마른체형')
    elif BMI < 25.0:
        print('표준')
    elif BMI < 30.0:
        print('비만')
    else:
        print('고도비만')

print("KG: 74, CM: 173")
getBMI(74, 173)


print('\n\n')
print('5-5')
'''
while True:
    getBMI(input('몸무게(kg): '), input('키(cm): '))
'''

print('\n\n')
print('5-6')
def get_triangle_area(width, height):
    return width*height/2
print("WIDTH: 20, HEIGHT: 10")
print(get_triangle_area(20, 10))


print('\n\n')
print('5-7')
def add_start_to_end(start, end):
    #return (start+end)/2 * (end-start+1)
     return sum(range(start, end+1))
print("START: 10, END: 17")
print(add_start_to_end(10, 17))


print('\n\n')
print('5-8')
input_list = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']
output_list = []
for item in input_list:
    output_list.append(item[:3])

print(output_list)
