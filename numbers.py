x = int(input('Please input min number: '))
y = int(input('Please input max number: '))
for i in range(x, y+1):
    if i % 2 == 0:
        print(i, end=', ')
        i += 1
