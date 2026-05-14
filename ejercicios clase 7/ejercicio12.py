"""12. Función que calcule el promedio de 3 notas
Situación: Crear una función que reciba 3 notas, calcule el promedio y lo devuelva."""

def promediar (n1,n2,n3):
    suma = n1 + n2 + n3
    promedio = suma/3
    return promedio

nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

print(f"El promedio de los siguientes números es: {nota1}, {nota2} y {nota3} es: {promediar(nota1, nota2, nota3)}")

"""def promediar():
    suma = 0
    for i in range(1,4,1): 
        nota = int(input("Ingrese un número: "))
        suma = suma + nota
        print(suma)

    promedio = suma / 3
    return promedio

print("El promedio de las 3 notas es: ", promediar())"""

"""def promediar(n):
    n = n / 3
    return n

suma = 0
for i in range(1,4,1): 
    nota = int(input("Ingrese una nota: "))
    suma = suma + nota
    print(suma)

print("El promedio de las 3 notas es: ", promediar(suma))"""