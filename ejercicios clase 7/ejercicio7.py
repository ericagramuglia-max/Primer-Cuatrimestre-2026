"""7. Suma acumulada hasta número negativo
Situación: Pedir números al usuario uno por uno e ir
sumándolos.
El programa debe continuar mientras los números sean
positivos (mayores o iguales a 0).
Cuando se ingrese un número negativo, se detiene y
muestra la suma total.
"""
numero = int(input("Ingrese un número: "))
suma = 0
while numero>=0 :
    suma = suma + numero
    numero = int(input("Ingrese un número: "))
    
input(suma)