cantidad = int(input('Ingrese el numero de notas a registrar: '))
acumuladorNotas = 0

for i in range(cantidad):
    nota = float(input(f'Ingrese la nota del corte {i + 1}: '))
    acumuladorNotas = acumuladorNotas + nota

promedio = acumuladorNotas / cantidad
print(promedio)
print('La nota final es: ', round(promedio,2))