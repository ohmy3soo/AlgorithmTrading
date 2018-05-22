from pandas import Series, DataFrame
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# pandas Series
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
print('\n')



# pandas DataFrame

raw_data = {'col0': [1, 2 ,3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}
data = DataFrame(raw_data)
print(data)
print('\n')
print(data['col2'])     # Name: col2, dtype: int64
print(type(data['col0']))   # <class 'pandas.core.series.Series'>
print('\n')

daeshin = {'open': [11650, 11100, 11200, 11100, 11000],
           'high': [12100, 11800, 11200, 11100, 11150],
           'low': [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)      # 키가 사전 순
print('\n')

daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'])
print(daeshin_day)
print('\n')

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)      # size가 맞아야 함
print(daeshin_day)
print('\n')

close = daeshin_day['close']
print(close)
print('\n')
#print(daeshin_day['16.02.24'])     # Error 칼럼의 키 값으로 판단

day_data = daeshin_day.ix['16.02.24']
print(day_data)
print(type(day_data))   # <class 'pandas.core.series.Series'>
print('\n')
# 칼럼에 접근하려면 칼럼 이름 지정
# 로우에 접근하려면 ix메서드 이용해 인덱스 값 지정
print(daeshin_day.columns)
print(daeshin_day.index)



# 주식 데이터 받기


gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
new_gs = gs[gs['Volume'] != 0]

ma5 = new_gs['Adj Close'].rolling(window=5).mean()
ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()

new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['Adj Close'], label='Adj Close')
plt.plot(new_gs.index, new_gs['MA5'], label='MA5')
plt.plot(new_gs.index, new_gs['MA20'], label='MA20')
plt.plot(new_gs.index, new_gs['MA60'], label='MA60')
plt.plot(new_gs.index, new_gs['MA120'], label='MA120')


plt.legend(loc="best")
plt.grid()
plt.show()