import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio.
    Args:
        radio (float): El radio del círculo.
    Returns:
        float: El área del círculo.
    """
    area = math.pi * radio**2
    return area

# Obtener el radio del usuario como un número de punto flotante
radio_str = input("Ingrese el radio del círculo: ")
radio = float(radio_str)

# Calcular el área y mostrarla al usuario
area = calcular_area_circulo(radio)
print(f"El área del círculo es: {area:.2f}")