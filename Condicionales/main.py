# Condicionales (if)
# Evalua una expresion logica y ejecuta el codigo indicado, segun la expresion indicada
# Si no se cumple la condicion, dentro del if, se ejecuta la condicion else.

numero1 = 32
numero2 = 35

if 32 == 35:
    print('true')
elif 32 > 35:
    print('true is greather')
elif 32 < 35:
    print('true is less')
else:
    print('The function es no assign')

#Se debe tener en cuenta los espacios dentro del If, 
#Esto debido a que python toma la logica de un if sengun
#los espacios a la derecha
print('/******** Logica de IF **********/')

edad = int(input('Digita tu edad: '))

if edad >= 18:
    print('Es mayor de edad')
    if edad >= 65:
        print('Es adulto mayor')
else:
    if edad >= 12:
        print('Es un adolecente')
    else:
        print('Es un niño')

# Operadores logicos
# AND = Excluyente
# OR = Incluyente

print('/******** Operadores Logicos **********/')

# Rangos
if edad >= 18 or edad <= 50:
    print('Es habilitado para las elecciones')
else:
    print('No esta habilitado para las elecciones')

# Intervalos
if 18<= edad <=50:
    print('Esta habilitado')
else:
    print('No esta habilitado')