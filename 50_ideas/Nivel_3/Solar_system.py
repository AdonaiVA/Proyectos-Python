from math import pi
from random import choice as ch


planets = [     
            'Mercury',
            'Venus',
            'Earth',
            'Mars',
            'Saturn'
            ]

random_planet = ch(planets)
radio = 0

if random_planet == 'Mercury':
  radio = 2440
elif random_planet == 'Venus':
  radio = 6052
elif random_planet == 'Earth':
  radio = 6371
elif random_planet == 'Mars':
  radio = 3390
elif random_planet == 'Saturn':
  radio = 58232
else:
  print('Oops! An error occurred.')


planet_area = round(4 * pi * radio * radio)

print(f'Your Planet is {random_planet} and the area is: {planet_area} km2')