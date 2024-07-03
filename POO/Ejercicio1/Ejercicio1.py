# Escribir un programa que pregunte el nombre completo del usuario en la consola e 
# imprima en formato donde la primera letra es mayúscula y los demás minúscula.

#Ejemplo:
#nombre ingresado: jimmy farfan
#outPut: Jimmy Farfán

# Se solicita el nombre
nombre = input('Registra tu Nombre: ')
# Se realiza el formato del texto
formato = nombre.title()
# Se imprime el formato
print(formato)