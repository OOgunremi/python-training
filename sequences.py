import re


# Question 1: Answer = 4

# Question 2: Answer = ['john', 'peter']

# Question 3:
def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 6:
            print("Make sure your password is at least 6 letters")
        elif len(password) > 12:
            print("Make sure your password is not more than 12 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
        elif re.search('[$#@]', password) is None:
            print("Your password must include either $, #, @ in it")
        else:
            print("Your password seems fine")
            break

validate()


# Question 4:

a = [4, 7, 3, 2, 5, 9]
for i, item in enumerate(a):
    print(i, ',', item)


# Question 5:
def print_even():
    word = input('Type in strings: ')
    i = 0
    while i < len(word) + 1:
        print(word[i])
        i = i + 2

print_even()

# Question 6:
def reverse():
    word = input('Type in strings: ')
    i = len(word) - 1
    while i >= 0:
        print(word[i], end= '')
        i -= 1


reverse()


# Question 7:
