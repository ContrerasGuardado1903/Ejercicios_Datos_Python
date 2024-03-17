"""Calcular suledo neto y Descuentos
Nombre: Samuel Ernesto Contreras Centeno"""

# Datos Personales

nombreUsuario = input("Ingrese su nombre: ")
apellidoUsuario = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
sueldoBase = float(input("Ingrese su sueldo base: "))

# Operaciones con Descuento

descuentoImpuesto = sueldoBase * 0.10
descuentoSeguro = sueldoBase * 0.05
sueldoNeto = sueldoBase - descuentoImpuesto - descuentoSeguro

# Impresion

print(f"Nombre: {nombreUsuario} {apellidoUsuario}")
print(f"Edad: {edad}")
print(f"Sueldo Base: {sueldoBase}")
print(f"Descuento por impuestos: {descuentoImpuesto}")
print(f"Descuento por seguro: {descuentoSeguro}")
print(f"Sueldo neto: {sueldoNeto}")

input("Presione Enter para salir...")