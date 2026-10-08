print ("PRECIO FINAL DEL PRODUCTO")

# Línea de separación
print("-" * 40)

# Definimos el porcentaje de IVA
PorcentajeIva = 19

# input() pide el nombre del producto
Producto = input("Digite el nombre del producto: ")

# float() convierte el precio en un número decimal
Precio = float(input("Digite el precio sin IVA: "))

# Calculamos el valor del IVA
Iva = Precio * PorcentajeIva / 100

# Calculamos el precio final
PrecioFinal = Precio + Iva

# Línea de separación
print("-" * 40)

# Mostramos los resultados
print("Producto:", Producto)
print("Precio sin IVA:", round(Precio, 2))
print("Porcentaje de IVA:", PorcentajeIva, "%")
print("Valor del IVA:", round(Iva, 2))
print("Precio con IVA:", round(PrecioFinal, 2))