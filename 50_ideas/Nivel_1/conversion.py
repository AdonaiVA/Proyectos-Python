import math

print('-'*40)
print('Convertidor métrico'.center(40))
print('-'*40)
print('1. Kilometros')
print('2. Metros')
print('3. Feet')
print('4. Yarda')
print('5. Milla')

i = int(input('¿Qué unidad quieres convertir?:'))
c = int(input('¿En qué unidad la quieres convertir?:'))
cantidad = int(input('¿Cuántas undiades son?:'))

#Kilometros
    
if (i == 1) and (c == 2):
    resultado = cantidad * 1000 
    print('son ' + str(resultado) + ' Metros')
elif (i == 1) and (c == 3):
    resultado = cantidad * 3280.84 
    print('son ' + str(resultado) + ' Feet')
elif (i == 1) and (c == 4):
    resultado = cantidad * 1093.61 
    print('son ' + str(resultado) + ' Yarda')
elif (i == 1) and (c == 5):
    resultado = cantidad * .6213 
    print('son ' + str(resultado) + ' Milla')

# Metro
elif (i == 2) and (c == 1):
    resultado = cantidad * 0.001 
    print('son ' + str(resultado) + ' Kilometros')
elif (i == 2) and (c == 3):
    resultado = cantidad * 3.28 
    print('son ' + str(resultado) + ' Feet')
elif (i == 2) and (c == 4):
    resultado = cantidad * 1.093 
    print('son ' + str(resultado) + ' Yardas')
elif (i == 2) and (c == 5):
    resultado = cantidad * 0.0006213 
    print('son ' + str(resultado) + ' Millas')

# Feet
elif (i == 3) and (c == 1):
    resultado = cantidad * 0.0003048
    print('son ' + str(resultado) + ' Kilometros')
elif (i == 3) and (c == 2):
    resultado = cantidad * .3048 
    print('son ' + str(resultado) + ' Metros')
elif (i == 3) and (c == 4):
    resultado = cantidad * .33333 
    print('son ' + str(resultado) + ' Yardas')
elif (i == 3) and (c == 5):
    resultado = cantidad * 0.00018939 
    print('son ' + str(resultado) + ' Millas')

#Yardas

elif (i == 4) and (c == 1):
    resultado = cantidad * 0.0009144
    print('son ' + str(resultado) + ' Kilometros')
elif (i == 4) and (c == 2):
    resultado = cantidad * .9144
    print('son ' + str(resultado) + ' Metros')
elif (i == 4) and (c == 3):
    resultado = cantidad * 3
    print('son ' + str(resultado) + ' Feet')
elif (i == 4) and (c == 5):
    resultado = cantidad * 0.00056818
    print('son ' + str(resultado) + ' Millas')

# Milla

# Feet
elif (i == 5) and (c == 1):
    resultado = cantidad * 1.6093
    print('son ' + str(resultado) + ' Kilometros')
elif (i == 5) and (c == 2):
    resultado = cantidad * 1609.344
    print('son ' + str(resultado) + ' Metros')
elif (i == 5) and (c == 3):
    resultado = cantidad * 5280
    print('son ' + str(resultado) + ' Feet')
elif (i == 5) and (c == 4):
    resultado = cantidad * 1760
    print('son ' + str(resultado) + ' Yarda')
    
else:
    print('Te equivocaste en un dígito')
    

