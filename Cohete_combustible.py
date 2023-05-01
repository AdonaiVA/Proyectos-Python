import math

def distance_to_miles(i):
    distance = i * .6213712
    return distance

x = int(input('Kilometers: '))


print('Your miles are: ' + str(distance_to_miles(x)))