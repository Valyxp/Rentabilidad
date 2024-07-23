# Solicitar al usuario que ingrese el radio y la constante g 
r = float(input("Ingrese el radio en Kilómetros: ")) * 1000 # Convertir de Km a metros # 6371
g = float(input("Ingrese la constante g en [m/s^2]: ")) # 9.8

# Calcular la velocidad de escape usando la fórmula proporcionada
Ve = (2 * g * r) ** 0.5

# Mostrar el resultado 
print(f"La velocidad de Escape es {Ve:.1f} [m/s]") # Resultado 11174.6 [m/s]

# Ve : corresponde a la Velocidad de Escape en [m/s].
# g: corresponde a la constante gravitacional en [m/s2].
# r: Corresponde al radio del planeta en [m].