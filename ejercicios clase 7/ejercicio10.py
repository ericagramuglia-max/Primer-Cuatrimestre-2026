"""FUNCIONES
10. Función que calcule el área de un rectángulo
Situación: Crear una función que reciba base y altura
y devuelva el área del rectángulo.
"""

def area_rectangulo(b,a):
    area = b * a
    return area

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))
resultado = area_rectangulo(base,altura)
print("El área es: ", resultado)

