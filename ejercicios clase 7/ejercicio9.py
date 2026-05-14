"""9. Calcular el promedio de 4 notas
Situación: El programa debe pedir al usuario 4 notas
(una por una), sumarlas y calcular el promedio final.
Mostrar el promedio al finalizar."""

suma_notas = 0
for i in range(1,5,1):
    nota = int(input("Ingrese la nota: "))
    suma_notas = suma_notas + nota
promedio = suma_notas/4
print ("El promedio de las notas es: ", promedio)