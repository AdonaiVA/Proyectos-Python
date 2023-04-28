import math

figura = int(input("Cuantos lados tiene la figura?\n*****:"))

if figura == 3:
    base = int(input('¿Cuánto mide la base? '))
    altura = int(input('¿Cuánto mide la altura? '))
    area = (base * altura) / 2
    print('El área de tu triangulo es:' + str(area))
elif figura == 4:
    base = int(input('¿Cuánto mide la base de la figura? '))
    altura =  int(input('¿Cuánto mide el ancho o el alto de tu figura? '))
    area = (base * altura)
    print('El área de tu triangulo es:' + str(area))   
elif figura == 1:
    radio = int(input('¿Cuánto mide el radio de tu circulo? '))
    area = (radio * radio) * (3.1416)
    print('El área de tu triangulo es:' + str(area)) 
