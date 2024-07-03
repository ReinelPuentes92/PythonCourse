#Dado una cadena con el siguiente formato de hora: hhmmss
#Imprimir el mensaje en formato: "Son las 18h:24min:50seg"

hora = input("Digita la hora en formato (hhmmss): ")
print("Son las "+ hora[0:2] + "h" + ":"+ hora[2:4] + "min"+ ":"+ hora[4:6] + "seg")