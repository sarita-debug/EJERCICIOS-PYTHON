print("MEDIDAS DE UN RECTÁNGULO")

# Línea de separación
print("-" * 40)

# float() convierte los datos en números decimales
Largo = float(input("Digite el largo en metros: "))
Ancho = float(input("Digite el ancho en metros: "))

# Calculamos el perímetro
Perimetro = 2 * (Largo + Ancho)

# Calculamos el área
Area = Largo * Ancho

# Línea de separación
print("-" * 40)

# Mostramos los resultados
print("Largo:", Largo, "m")
print("Ancho:", Ancho, "m")
print("Fórmula del perímetro: 2 x (largo + ancho)")
print("Perímetro:", round(Perimetro, 2), "m")
print("Área:", round(Area, 2), "m²")