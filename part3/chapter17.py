import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

con = sqlite3.connect("kospi.db");
print(type(con))


cursor = con.cursor()
#cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volumn int)")
#cursor.execute("INSERT INTO kakao VALUES('16.06.04', 93000, 98100, 96300, 94000, 321421)")
#cursor.execute("INSERT INTO kakao VALUES('16.06.06', 91000, 98000, 96300, 94000, 321455)")
#con.commit()

cursor.execute("SELECT * FROM kakao")

'''
for i in range(3):
    print(cursor.fetchone())

# 앞에서 fetch하고 남은 것들
print(cursor.fetchall())
'''
kakao = cursor.fetchall()
print(kakao[0][0])
con.close()