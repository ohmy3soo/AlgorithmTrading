

a = 255
b = 255
print(id(a), id(b))
# --> 인터프리터에서도 같게 나온다

a = 12345612123123
b = 12345612123123
print(id(a), id(b), end='\n\n')
# --> 인터프리터에서는 다르게 나온다


# 문자열
my_jusik = 'naver daum'
split_jusik = my_jusik.split(' ')
print(split_jusik[0])
print(my_jusik[-4:], end='\n\n')


daum = 'Daum'
kakao = 'KaKao'

daum_kakao = daum + ' ' + kakao
print(daum_kakao, end='\n\n')


########## 연습 문제 ##########

print('2-1')
daum_price = 89000
naver_price = 751000

amount = daum_price*100 + naver_price*20
print(amount, end='\n\n')


print('2-2')
loss = (daum_price*0.05)*100 + (naver_price*0.1)*20
print(loss, end='\n\n')


print('2-3')
F = 50
C = (F-32)/1.8
print(C, end='\n\n')


print('2-4')
output = 'pizza\n'
print(output*10, end='\n\n')


print('2-5')
mon_closing_naver_price = 1000000 * 0.7
tue_closing_naver_price = mon_closing_naver_price * 0.7
wed_closing_naver_price = tue_closing_naver_price * 0.7
print(wed_closing_naver_price, end='\n\n')


print('2-6')
print('이름: {} 생년월일: {} 주민등록번호 {}'.format('파이썬', '2014년 12월 12일', '20141212-1623210'),
      end='\n\n')


print('2-7')
s = 'Daum KaKao'
new_s = s.split()[1] + ' ' + s[0:4]
print(new_s, end='\n\n')


print('2-8')
a = 'hello world'
a = 'hi'+ ' ' + a[-5:]
print(a, end='\n\n')


print('2-9')
x = 'abcdef'
x = x[1:] + x[0]
print(x, end='\n\n')