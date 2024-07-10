# Variables
ABC = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
concatenacion = ''

# Solcitud de Nombre
nombre = input('Ingrese su nombre: ').upper()

# Recorremos los valores del nombre
for i in nombre:
    codigo = ABC.find(i)+1
    if codigo < 10:
        concatenacion = concatenacion + '0'+str(codigo)
    else:
        concatenacion = concatenacion + str(codigo)

print('Su numero de matricula es: ' + concatenacion)