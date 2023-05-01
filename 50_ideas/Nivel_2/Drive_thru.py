menu = ['1.Hamburguesa',
        '2.Papas a la francesa',
        '3.Hot Dog',
        '4.Refresco',
        '5.Birria',
        '6.Ramen',
        '7.Galletas',
        '8.Palomitas',
        '9.Cheetos',
        '10.Dulces'
       ]

def index(i):
    return menu[i-1]

def welcome():
    return print('Hi!\nWelcome to McBrutus\nThis is our menu:')

def opciones():
    for i in range(len(menu)):
        print(menu[i])
    return

def pedido():
    x = int(input('What you want?\n*****:'))
    print(index(x))
    if x == 1:
        print('Serían $50 pesos')
    if x == 2:
        print('Serían $25 pesos')
    if x == 3:
        print('Serían $20 pesos')
    if x == 4:
        print('Serían $20 pesos')
    if x == 5:
        print('Serían $50 pesos')
    if x == 6:
        print('Serían $40 pesos')
    if x == 7:
        print('Serían $20 pesos')
    if x == 8:
        print('Serían $20 pesos')
    if x == 9:
        print('Serían $20 pesos')
    if x == 10:
        print('Serían $20 pesos')
    return 

welcome()
opciones()
pedido()





