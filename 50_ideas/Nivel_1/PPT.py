import random

opciones = ['piedra', 'papel', 'tijera']

print('-' * 30)
print('Piedra, papel o tijera'.center(30))
print('-' * 30)
print('1. Piedra')
print('2. Papel')
print('3. Tijera')

humano = int(input('\nIngrese una opción del 1 al 3: '))
pc = random.randint(1,3)

resultado = print('\nVos elegiste ' + opciones[humano - 1] + '.\n')
resultado2 = print('La computadora eligió ' + opciones[pc - 1] + '.\n')

if (humano == 1)and(pc == 1):
    print('Empate')
elif (humano == 1)and(pc == 2):
    print('Perdiste')
elif (humano == 1)and(pc == 3):
    print('Ganaste')
elif (humano == 2)and(pc == 1):
    print('Ganaste')
elif (humano == 2)and(pc == 2):
    print('Empate')
elif (humano == 2)and(pc == 3):
    print('Perdiste')
elif (humano == 3)and(pc == 1):
    print('Perdiste')
elif (humano == 3)and(pc == 2):
    print('Ganaste')
elif (humano == 3)and(pc == 3):
    print('Empate')


