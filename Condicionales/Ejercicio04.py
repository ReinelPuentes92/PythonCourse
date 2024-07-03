# Una tienda vende un producto a precios unitarios que dependen de la cantidad
# De unidades adquiridas de acuerdo a la siguiente tabla

# Captura el numero de productos a comprar
print('/***** Calculo de Importes *****/')
cantidad = int(input('Digete la cantidad a comprar: '))

# Descuentos
# 1. Si el cliente adquiere mas de 50 unidades, la tienda le descuenta el 15%. SI NO, solo le descuenta el 5%.

if 1<= cantidad <=25:
    precio = 27.7
    descuento = '5%'
elif 26<= cantidad <=50:
    precio = 25.5
    descuento = '5%'
elif 51<= cantidad <=75:
    precio = 23.7
    descuento = '15%'
else:
    precio = 21.7
    descuento = '15%'

if cantidad > 50:
    importeParcial = cantidad * precio
    importeDescuento = importeParcial * 0.15
    importeTotal = importeParcial - importeDescuento
else:
    importeParcial = cantidad * precio
    importeDescuento = importeParcial * 0.5
    importeTotal = importeParcial - importeDescuento


# Imprime
print('El valor por unidad es:', precio, sep=' ')
# 1. Importe de la compra
print('El valor parcial es:', importeParcial, sep=' ')
print('El porcentaje de descuento es:', descuento, sep=' ')
# 2. Importe del descuento
print('El descuento es:', importeDescuento, sep=' ')
# 3. Importe a pagar
print('El valor a pagar es:', importeTotal, sep=' ')