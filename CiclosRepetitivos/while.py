# While: Repite la ejecucion del codigo hasta que se cumpla la condicion.

print('/***** While *****/')
contador = 1
numeroAlumnos = int(input('Registra el numero de alumnos a ingresar: '))
while contador <= numeroAlumnos:
    nombre = input('Registre su Nombre: ')
    print('Se ha registrado el alumno', contador)
    contador += 1

print('/***** Acumulador *****')
alumnos = int(input('Ingrese el numero de notas a registrar: '))
contador = 1
totalNotas = 0
promedio = 0

while contador <= alumnos:
    nota = int(input(f'Ingrese la nota del alumno {contador}: '))
    totalNotas = totalNotas + nota
    print('El valor total de notas es: ', totalNotas)
    contador += 1

promedio = totalNotas / alumnos
print('El promedio de notas es: ', promedio)

contador = 1
promedioSalarial = 0
totalSueldos = 0

colaboradores = int(input('¿Cuantos colaboradores son parte de la empresa?: '))

while contador <= colaboradores:
    sueldo = float(input(f'Sueldo del empleado {contador}: '))
    totalSueldos = totalSueldos + sueldo
    contador += 1

promedioSalarial = totalSueldos / colaboradores
print('El promedio salarial es: ', promedioSalarial)


