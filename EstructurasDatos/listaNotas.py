# Declaro las variables
sabana = []

# Solicito cantidad de notas
cantidad = int(input('Ingrese la cantidad de notas a registrar: '))

# Registro de notas
for i in range(cantidad):
    nota = float(input(f'Ingrese nota {i + 1}: '))
    sabana.append(nota)   

# Calculo de notas
notasTotales = len(sabana)
notaMayor = max(sabana)
notaMenor = min(sabana)
promedioTotal = sum(sabana) / notasTotales

# Resultados
print('Notas registradas: ', notasTotales)
print('La Nota mayor es: ', notaMayor)
print('La nota menor es: ', notaMenor)
print('El promedio general es: ', round(promedioTotal,2))
