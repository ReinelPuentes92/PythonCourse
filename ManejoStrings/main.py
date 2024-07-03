#Secuencia de caracteres alfanumericos que representan un texto. se escribe con comilla sencilla ' o comilla doble "
my_string = 'Aprender Python!'
another_string = "Puede ser dificil al comienzo pero nada me puede quedar grande"

along_string = '''
Hola,
Estoy aprendiendo python
voy paso a paso
'''

##print(along_string)

#Cada caracter tiene asociado una posicion un índice que permite acceder a él
palabra = 'El HOMBRE araña'
#para imprimir un solo caracter
#print(palabra[0:1+1])
#para imprimir un grupo de caracteres
#regla de python: la ultima posicion el compilador le resta -1, para tomar la ultima posicion de le debe sumar +1 
#print(palabra[3:9])
#Para imprimir de izquierda a derecha se debe contar desde la posicion negativa, cuando se deja solo los :
#Quiere decir que debe tomar todas las posiciones que se encuentren desde la ubicacion inicial a la derecha
#print(palabra[-5:])
#print(palabra[-12:-6])

#Operaciones con las cadenas
#concatenacion
c1 = "Reinel"
c2 = 'Puentes'
c3 = '''
Reinel Puentes es un programador con perfil fullstack
'''
c4 = 'Fernando'
print(c1 + c2)
#repeticion de una cadena
print(c1 * 2)
#si una cadena se encuentra en un texto
print(c1 in c3)
#si una cadena no se encuentra en una cadena de texto
print(c1 not in c3)