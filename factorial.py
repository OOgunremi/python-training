def factorial(x):
    print('The factorial of ',x, ' is: ')
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=' ')
            if i % 2 == 0:
                print('even')
            else:
                print('odd')

num = 24

factorial(num)