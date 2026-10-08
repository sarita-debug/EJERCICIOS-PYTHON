print("AREA DE UN TRIANGULO")
print("-" * 40)

# Pedimos la base y la altura del triángulo
Base = float(input("Digite la base del triángulo: "))
Altura = float(input("Digite la altura del triángulo: "))

# Calculamos el área del triángulo
Area = (Base * Altura) / 2

# Mostramos el resultado
print("-" * 40)
print("Base del triángulo:", Base)
print("Altura del triángulo:", Altura)
print("Formula aplicada: (Base * Altura) / 2")
print("Área del triángulo:", round(Area, 2))