# Advertencia al usuario
print("Advertencia: Asegúrese de ingresar valores válidos para evitar errores.")

# Solicitar al usuario que ingrese los datos
P = float(input("Ingrese el precio de suscripción: ")) # Precio de Suscripción
U = int(input("Ingrese el número de usuarios normales: ")) # Número de Usuarios
GT = float(input("Ingrese los gastos totales: ")) # Gastos Totales
Uanterior = float(input("Ingrese las utilidades del año anterior: ")) # Utilidades del año anterior

# Calcular las utilidades actuales
Uactuales = P * U - GT

# Calcular la razón entre las utilidades actuales y las utilidades del año anterior
Razon = Uactuales / Uanterior

# Mostrar los resultados
print(f"Las utilidades del proyecto son: {Uactuales:.2f}")
print(f"La razón entre las utilidades actuales y las del año anterior es {Razon:.2f}")



