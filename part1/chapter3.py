
print('\n\n')
print("="*10 + "LIST" + "="*10)

kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽',
               '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']

print('시가총액 5위: ', kospi_top10[4])

kospi_top5 = kospi_top10[0:5]
print(kospi_top5)
print(kospi_top10[:5])
print(kospi_top10[5:])


#kospi_top11 = kospi_top10.append('SK텔레콤')
#print(kospi_top11)     # --> None

kospi_top10.append('SK텔레콤')
kospi_top11 = kospi_top10
print(kospi_top11)

kospi_top10.pop()
print(kospi_top10)
kospi_top10.insert(3, 'SK텔레콤')
print(kospi_top10)


print(kospi_top10[-1])
del kospi_top10[-1]
print(kospi_top10)
print(len(kospi_top10))



print('\n\n')
print("="*10 + "TUPLE" + "="*10)

# 튜플은 튜플 내 원소를 변경할 수 없다.
# 튜플은 리스트보다 속도가 빠르다.
# --> 한번 데이터를 저장해둔 후 추가하거나 삭제할 필요가 없는 경우라면
#       되도록 리스트보다는 튜플을 사용하자!

t = ('Samsung', 'LG', 'SK')
print(t[0:2])
#t[0] = 'NAVER'     # ERROR



print('\n\n')
print("="*10 + "DICTIONARY" + "="*10)
# '종목': '종목에 대한 현재가'
cur_price = {}
print(type(cur_price))
cur_price['daeshin'] = 30000
print(cur_price)

cur_price['Daum KAKAO'] = 80000
print(cur_price)
print(len(cur_price))
# 딕셔너리는 데이터를 순서대로 저장하는 것이 아니라
# 키와 값의 쌍이 서로 연결되도록만 저장하기 때문에
# 인덱싱을 지원하지 않는다.
# 키를 통해 데이터를 얻는다.

# append, insert같은 메서드를 지원하지 않는다.
cur_price['naver'] = 800000
del cur_price['daeshin']
print(cur_price)
cur_price['daeshin'] = 30000

print('cur_price.keys(): ', cur_price.keys())

stock_list = list(cur_price.keys())
print(stock_list)
price_list = list(cur_price.values())
print(price_list)

if 'Samsung' in cur_price.keys():
    print("'Samsung' is in cur_price.keys()")
else:
    print("'Samsung' is not in cur_price.keys()")


myDict = {'a': 1, 'b': 2, 'c': 3, 'a':4}
print(myDict['a'])      # 4
# value를 통해 key를 찾으려면 반복문을 통해 하나하나 확인해야 한다.
