# El uso del break se da en una condicion de bucle infinito
alumnos = 5
contador = 1
acumulador = 0

while contador <= alumnos:
    nota = float(input(f'Ingrese la nota del alumno {contador}: '))
    if nota < 0:
        break
    acumulador = acumulador + nota
    print('VAlor total de notas: ', acumulador)
    contador += 1

print('Recuerde!, la nota no debe ser menor a 0')


# El uso del continue lo que realiza es saltar dentro del buble una condicion que le especifiquemos
alumnos = 5
contador = 1
acumulador = 0

while contador <= alumnos:
    nota = float(input(f'Ingrese la nota del alumno {contador}: '))
    if nota < 0:
        continue
    acumulador = acumulador + nota    
    print('Valor total de notas: ', acumulador)
    contador += 1

print('Recuerde!, la nota no debe ser menor a 0')