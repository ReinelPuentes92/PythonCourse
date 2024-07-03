# Categorizar los postulantes en funcion del sexo y de la edad de acuerdo con las siguientes indicaciones
# 1. SI la persona es de sexo F, categoria FA y si tiene menos de 23 años y FB, en caso contrario.
# 2. SI la persona es de sexo M, categoria MA sitiene menos de 25 años y MB, en caso contrario.
# Diseñe un programa que determine su categoria.

# Captura el sexo
print('/***** Segun su sexo digite *****/')
print('F: Femenino')
print('M: Masculino')
sexo = input('Digite su sexo: ').upper()
edad = int(input('Digite su edad: '))

# Se determina la categoria
# 1. SI es F y tiene menos de 23 años categoria FA. SI NO, si es mayor a 23 años categoria FB.
# 2. SI es M y tiene menos de 25 años categoria MA. SI NO, si es mayor a 25 años categoria MB.

if (sexo == 'F') and (18<= edad <23):
    print('Su categoria es FA')
elif (sexo == 'F') and (edad >= 23):
    print('Su categoria es FB')
elif (sexo == 'M') and (18<= edad <25):
    print('Su categoria es MA')
elif (sexo == 'M') and (edad >= 25):
    print('Su categoria es MB')
else:
    print('Su edad no tiene categorización')