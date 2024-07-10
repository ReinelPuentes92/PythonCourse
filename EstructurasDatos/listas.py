# Para crear una lista
lista = list('hola reinel')
listaNumerica = [0,12,14,15,12]

# Para acceder a la posicion
posicion = listaNumerica[2]

# tomar rango de posiciones, se realiza a traves de los intervalos
intervaloStrings = lista[0:3+1]
intervaloAbierto = lista[5:]

#print(intervaloAbierto)

# Sublistas = equeñas listas de diferentes tipos dentro de la lista
sublist = [0,1,2,[3,4,[1,2]],5,6]
intervalo = sublist[3][2][1]
sublist_1 = sublist[3]
sublist_2 = sublist[3][2]
#print(max(sublist_2))

#print(listaNumerica.count(12))

# Relaciond de listas
#c = ['a', 'hash', [False, 34]]
#b = ['asdfg', [False, True, -4.56], 90]

#d = c + b
#print(d)

#e = str(d).replace('[','').replace(']','').replace(' ','')
#print(str(e))

# extend
a = [1,2,3]
b = [4,5,6]
a.extend(b)

# append
a.append(7)

# remove
a.remove(2)

# Reverse
a.reverse()
print(a)
