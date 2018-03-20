
def cal_upper(price):
    increament = price * 0.3
    upper_price = price + increament
    return upper_price


def cal_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement
    return lower_price

author = "pystock"

if __name__ == "__main__":
    print(cal_upper(10000))
    print(cal_lower(10000))
    print(__name__)
'''
13000.0
7000.0
__main__
'''

# 독립적으로 실행됐다면 __name__ == __main__
# 다른 파일에 임포트된 경우에는 __name__ == 자신의 파일명