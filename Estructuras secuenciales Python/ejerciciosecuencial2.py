print("PROMEDIO DE TRES NOTAS")
print("-" * 40)

# Pedimos el nombre del estudiante
Estudiante = input("Digite el nombre del estudiante: ")

# Pedimos las tres notas
# float() convierte el dato en número decimal
Nota1 = float(input("Digite la nota 1: "))
Nota2 = float(input("Digite la nota 2: "))
Nota3 = float(input("Digite la nota 3: "))

# Sumamos las tres notas
Suma = Nota1 + Nota2 + Nota3

# Calculamos el promedio dividiendo la suma entre 3
Promedio = Suma / 3

# Mostramos los resultados
print("-" * 40)
print("Estudiante:", Estudiante)
print("Nota 1:", Nota1)
print("Nota 2:", Nota2)
print("Nota 3:", Nota3)
print("Suma de las notas:", round(Suma, 2))
print("Promedio:", round(Promedio, 2))