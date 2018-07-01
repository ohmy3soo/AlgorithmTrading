import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web
import sqlite3
import datetime



'''

# 17_2_2 SQLite DB에서 테이블 로드하기

raw_data = {'col0': [0, 1, 2, 3],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

df = DataFrame(raw_data)

#    col0  col1  col2
# 0     1    10   100
# 1     2    20   200
# 2     3    30   300
# 3     4    40   400


con =sqlite3.connect("kospi.db")
#df.to_sql('test2', con)

# con 객체 전달, index_col -> DataFrame 객체에서 인덱스로 사용될 칼럼을 지정하는 것
df = pd.read_sql("SELECT * FROM test", con, index_col=None)
print(df)
df = pd.read_sql("SELECT * FROM test", con, index_col='col0')
print(df)
con.close()

'''

# 17_2_3 Pandas를 이용한 주가 데이터 저장

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 12)
df = web.DataReader("078930.KS", "yahoo", start, end)

con = sqlite3.connect("kospi.db")
df.to_sql('078930', con, if_exists='replace')

readed_df = pd.read_sql("SELECT * FROM '078930'", con, index_col = 'Date')
