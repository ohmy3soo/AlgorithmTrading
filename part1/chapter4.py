


print(type(range(0,11)))
for i in list(range(0,11)):
    print(i)

for i in range(0,11):
    print(i)

# 결과는 같지만 후자가 메모리 사용관점에서 더 효율적



interest_stocks = {"Naver": 10, "Sanmsung":5, "SK Hynix":30}

for company, stock_num in interest_stocks.items():
    print("%s: Buy %s" %(company, stock_num))
for company in interest_stocks:
    print(company, type(company))       # key만 넘어온다


# while ==> 반복해야 할 횟수가 특별히 정해지지 않고 어떤 조건을 충족하는
#           동안만 실행도리 때 주로 사용한다.



apart = [[101, 102, 103, 104],
         [201, 202, 203, 204],
         [301, 302, 303, 304],
         [401, 402, 403, 404]]

for floor in apart:
    for room in floor:
        print(room)

# 파이썬에서는 자바처럼 중첩루프에서 특정루프로 break할 수 있는 방법이 없을까...