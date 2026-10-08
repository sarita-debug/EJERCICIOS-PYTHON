print("TOTAL DE LA COMPRA")
# Linea de separacion
print("-" * 40)

# Pedimos los datos del producto
# Input()pide un dato al ususario y lo guarda en una variable
Producto = input("Digite el nombre del producto: ")

# int() convierte el dato ingresado a un número entero
Cantidad = int(input("Digite la cantidad de productos: "))

# float() convierte el dato ingresado a un número decimal
PrecioUnitario = float(input("Digite el precio unitario: "))

# Calculamos el subtotal, el iva y el total de la compra
Subtotal = Cantidad * PrecioUnitario
Iva = Subtotal * 0.19
Total = Subtotal + Iva

# Mostramos los resultados
print("-" * 40)
print("Producto:", Producto)
print("Cantidad:", Cantidad)
print("Precio unitario:", PrecioUnitario)
print("Subtotal:", round(Subtotal, 2))
print("Iva (19%):", round(Iva, 2))
print("Total de la compra:", round(Total, 2))