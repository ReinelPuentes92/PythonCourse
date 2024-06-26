#Ingreso de datos
Nombre = input("Ingresa tu Nombre: ")
Apellido = input("Ingresa tu Apellido: ")
FechaNacimiento = input("Ingresa tu Fecha Nacimiento: ")
Edad = input("Ingresa tu Edad: ")
notaParcial = float(input("Ingresa tu nota Parcial: "))
notaFinal = float(input("Ingresa tu nota Final: "))

print("Hola", Nombre, Apellido, "Con Fecha de Nacimiento", FechaNacimiento, "Edad", Edad, end='\n')
print("Nota Parcial", notaParcial, "Nota Final", notaFinal)