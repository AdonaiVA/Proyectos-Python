import math


stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]

def price_at(i):
  return stock_prices[i-1]

def max_price(a, b):
  mx = 0
  for i in range(a, b):
    mx = max(mx, price_at(i))
  return mx

def min_price(a, b):
  mn = price_at(a)
  for i in range(a, b):
    mn = min(mn, price_at(i))
  return mn


a = int(input('Start day: '))
b = int(input('Last day: '))
c = int(input('Selected day: '))

print(max_price(a, b))
print(min_price(a, b))
print(price_at(c))