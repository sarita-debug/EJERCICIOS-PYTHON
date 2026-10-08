print("CONVERSION DE TEMPERATURA")
print("-" * 40)

# Pedimos la ciudad y la temperatura en grados Celsius
Ciudad = input("Digite el nombre de la ciudad: ")
Celsius = float(input("Digite la temperatura en grados Celsius: "))

# Convertimos celsius a Fahrenheit 
Fahrenheit = (Celsius * 9/5) + 32

# Convertimos celsius a kelvin
Kelvin = Celsius + 273.15

# Mostramos los resultados
print("-" * 40)
print("Ciudad:", Ciudad)
print("Temperatura en grados Celsius:", Celsius)
print("Temperatura en grados Fahrenheit:", round(Fahrenheit, 2))
print("Temperatura en grados Kelvin:", round(Kelvin, 2))