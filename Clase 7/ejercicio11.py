"""11. Función que determine si un número es par
Situación: Crear una función que reciba un número y
devuelva True si es par, False si es impar.
"""
numpar = True

def definir_par (numpar):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        numpar = True
    else:
        numpar = False
    return numpar 

print("TRUE si es par, FALSE si es impar: ", definir_par(numpar))
