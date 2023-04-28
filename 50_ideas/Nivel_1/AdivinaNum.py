import random

numeroSistema = random.randint(1, 10)

numeroUser = int(input('Adivina un número del 1 al 10:'))

if numeroSistema == numeroUser:
    print("Has adivinado :)")
else:
    print("No has adivinado :C el número era: " + str(numeroSistema))
