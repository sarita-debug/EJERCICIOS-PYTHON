print("CONVERSIÓN DE TIEMPO")

# Línea de separación
print("-" * 40)

# int() convierte el dato en un número entero
Minutos = int(input("Digite la cantidad de minutos: "))

# Calculamos las horas completas
Horas = Minutos // 60

# Calculamos los minutos que sobran
MinutosRestantes = Minutos % 60

# Convertimos los minutos a horas decimales
HorasDecimales = Minutos / 60

# Línea de separación
print("-" * 40)

# Mostramos los resultados
print("Minutos digitados:", Minutos)
print("Equivale a:", Horas, "horas y", MinutosRestantes, "minutos")
print("En formato decimal:", round(HorasDecimales, 2), "horas")