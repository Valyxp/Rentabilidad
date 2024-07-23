# Solicitar al usuario que ingrese los datos
P = float(input("Ingrese el precio de suscripción para usuarios normales: ")) # Precio de Suscripción
Unormal = int(input("Ingrese el número de usuarios normales: ")) # Usuarios normal 
Upremium = int(input("Ingrese el número de usuarios premium: ")) # Usuarios premium
GT = float(input("Ingrese los gastos totales: ")) # Gastos Totales

# Calcular el precio de suscripción para usuarios premium (50% mayor)
Ppremium = P + (0.5 * P)

# Calcular las utilidades
Utilidades = P * Unormal + Ppremium * Upremium - GT

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {Utilidades:.2f}")



