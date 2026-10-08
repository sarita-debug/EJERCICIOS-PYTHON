print("CALCULO DE EDAD")
print("-" * 40)

AnioActual = 2026
# Pedimos la fecha de nacimiento
Nombre = input("Digite el nombre de la persona: ")

# int() convierte el dato ingresado a un número entero
AnioNacimiento = int(input("Digite el año de nacimiento: "))

# Calculamos la edad

Edad = AnioActual - AnioNacimiento
Meses = Edad * 12
Dias = Edad * 365

# Mostramos el resultado
print("-" * 40)
print("Persona :", Nombre)
print("Año actual:", AnioActual)
print("Año de nacimiento:", AnioNacimiento)
print("Edad:", Edad)
print("Edad aproximada en meses:", Meses)
print("Edad aproximada en días:", Dias)