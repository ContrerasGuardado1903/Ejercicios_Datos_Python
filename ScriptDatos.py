"""Crear un Programa de Registro
Samuel Ernesto Contreras Centeno"""

# Datos Personales

nombre = input("Ingrese sus nombres: ")
apellido = input("Ingrese sus apellidos: ")
anioNacimiento = int(input("Ingrese su año de nacimiento: "))
salario = float(input("Ingrese su salario: "))

# Variable año

anio = 2024

# Calcular, edad y salario

edad = anio - anioNacimiento
salarioLiquido = salario * 0.10

# Impresion de nombre,apellido,edad y salarioLiquido

print("Su nombre es:", nombre, "-", "Su apellido es: ", apellido)
print("Su edad es: ",edad ,"años", "-" ,"Su salario liquido es: ", salarioLiquido)

input("Presione Enter para salir...")