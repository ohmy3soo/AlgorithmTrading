


# 01 파일 읽기

f = open('/Users/kihunahn/PycharmProjects/AlgorithmTrading/part1/buy_list.txt', 'rt')

# 파일을 읽어서 각 라인을 리스트에 넣은 후 리스트를 리턴
lines = f.readlines()
print(lines)

for line in lines:
    print(line, end='')

for line in lines:
    nline = line.split('\n')[0]
    print(nline)


input = 'My name is      Ahn ki hun '
words = input.split(' ')
for word in enumerate(words):
    print(word)

print('\n\n')
input = 'My name is      Ahn ki hun '
words = input.split()
for word in enumerate(words):
    print(word)


f.close()

# 02 파일 쓰기

f = open('/Users/kihunahn/PycharmProjects/AlgorithmTrading/part1/sell_list.txt', 'wt')
f.write('삼성전자\n')
f.write('SK하이닉스\n')
