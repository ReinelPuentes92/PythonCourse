#Obtener datos
edad = int(input('Ingresa tu edad: '))
peso = float(input('Ingresa tu peso: '))

#Calculo de la frecuencia
freq = 210 - 0.5 * edad - (0.01 * peso + 4)

#Resultado
print('Tu frecuencia cardiaca es: ', freq)