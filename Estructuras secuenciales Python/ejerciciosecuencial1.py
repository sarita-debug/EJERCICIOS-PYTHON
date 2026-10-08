print("LIQUIDACIÓN DE SALARIO")
print("-" * 40)

# Pedimos los datos del empleado
Empleado = input("Digite el nombre del empleado: ")

Horas = int(input("Digite las horas trabajadas: "))
ValorHora = int(input("Digite el valor de la hora: "))
                                                                                                                                                    
# Calculamos el salario bruto
SalarioBruto = Horas * ValorHora

# Calculamos el descuento de salud del 4%
Salud = SalarioBruto * 0.04

# Calculamos el descuento de pensión del 4%
Pension = SalarioBruto * 0.04

# Restamos los descuentos para obtener el salario neto
SalarioNeto = SalarioBruto - Salud - Pension


# Mostramos los resultados
print("-" * 40)
print("Empleado:", Empleado)
print("Horas trabajadas:", Horas)
print("Valor hora:", ValorHora)
print("Salario bruto:", round(SalarioBruto, 2))
print("Descuento salud (4%):", round(Salud, 2))
print("Descuento pensión (4%):", round(Pension, 2))
print("Salario neto a pagar:", round(SalarioNeto, 2))
print("Empleado:", Empleado, "Horas trabajadas:", Horas, "Salario bruto:", round(SalarioBruto, 2 )