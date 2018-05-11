from pandas import Series, DataFrame

mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

for stock in mystock:
    print(stock)


print('\n')

kakao_daily_closing_prices = [92300, 94300, 92100, 92400, 92600]
for price in kakao_daily_closing_prices:
    print(price)

kakao_daily_closing_prices = {'2016-02-19': 92600, '2016-02-18': 92400,
                              '2016-02-17': 92100, '2016-02-16': 94300, '2016-02-15': 92300}
print(kakao_daily_closing_prices['2016-02-19'])


print('\n')


# Series 기초
print(Series)
kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)
# index , value
print(kakao[0])
print(kakao[2])
print(kakao[4])


kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2016-02-19', '2016-02-18', '2016-02-17',
                                                            '2016-02-16', '2016-02-15'])
print(kakao2)

print(kakao2['2016-02-19'])
print(kakao2['2016-02-18'])

for date in kakao2.index:
    print(date)

for closing_price in kakao2.values:
    print(closing_price)


print('\n')


mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
merge = mine + friend
print(merge)

print(mine[2])
print(mine.index[1])
print(mine.index[:2])
#print(mine.index['sk'])
#mine.index[1] = 'ss'
mine.index = ['naver', 'ss', 'kt']
print(mine['ss'])
'''
mine = {'naver': 10, 'sk': 20, 'kt': 30}
friend = {'kt': 10, 'naver': 30, 'sk': 20}
merge = mine+friend
print(merge)
'''