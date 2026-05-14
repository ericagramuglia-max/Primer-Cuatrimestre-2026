"""14. Mostrar una tabla de multiplicar
Situación: Crear un procedimiento que reciba un número y muestre 
su tabla de multiplicar del 1 al 10."""

def multiplicar(n):

    for i in range(0,10,1):
        i = i + 1
        m = n * i
        print(f" {n} x {i} = {m}")

num = int(input("Ingresar el número para saber la tabla de multiplicar: "))
print(f"La tabla de multiplicar de {num} es: ")
print(multiplicar(num))