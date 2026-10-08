print("GASTO DE COMBUSTIBLE")

# Línea de separación
print("-" * 40)

# input() pide el nombre del carro
Carro = input("Digite el nombre del carro: ")

# float() convierte el dato en número decimal
Kilometros = float(input("Digite los kilómetros recorridos: "))

# float() convierte el dato en número decimal
Litros = float(input("Digite los litros consumidos: "))

# float() convierte el dato en número decimal
PrecioLitro = float(input("Digite el precio del litro: "))

# Calculamos el rendimiento del carro
Rendimiento = Kilometros / Litros

# Calculamos el gasto total
GastoTotal = Litros * PrecioLitro

# Calculamos el gasto por kilómetro
GastoPorKm = GastoTotal / Kilometros

# Línea de separación
print("-" * 40)

# Mostramos los resultados
print("Carro:", Carro)
print("Kilómetros recorridos:", Kilometros)
print("Litros consumidos:", Litros)
print("Rendimiento:", round(Rendimiento, 2), "km por litro")
print("Gasto total del combustible:", round(GastoTotal, 2))
print("Gasto por kilómetro:", round(GastoPorKm, 2))