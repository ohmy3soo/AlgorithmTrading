
# 함수를 만들 때 --> 함수의 입력, 출력, 함수의 동작을 파악

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
print(type(ret))        # <class 'tuple'>