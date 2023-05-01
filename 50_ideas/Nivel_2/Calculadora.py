import math

def add(a,b):
    x = a + b
    return x

def subtract(a,b):
    x = a-b
    return x

def multiply(a,b):
    x = a*b
    return x

def divide(a,b):
    x = a/b
    return x

def exp(a,b):
    x = a ** b
    return x

q = input('What you want?\n add\n subtract\n multiply\n divide\n exp\n *****:')

if q == 'add':
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(add(a,b))
elif q == 'subtract':
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(subtract(a,b))
elif q == 'multiply':
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(multiply(a,b))
elif q == 'divide':
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(divide(a,b))
elif q == 'exp':
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(exp(a,b))
else:
    print('SyntaxError')
