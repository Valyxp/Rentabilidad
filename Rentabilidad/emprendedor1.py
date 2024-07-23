# Solicitar al usuario que ingrese los datos
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))

# Calcular las utilidades
Utilidades = P * U - GT

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {Utilidades:.2f}")

# P: Precio de Suscripción
# U: Número de Usuarios
# GT: Gastos Totales