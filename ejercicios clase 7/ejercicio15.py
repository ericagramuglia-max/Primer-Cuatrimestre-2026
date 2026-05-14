"""15. Imprimir un menú de opciones
Situación: Crear un procedimiento que muestre un menú
con tres opciones:
1. Ver datos
2. Modificar datos
3. Salir
Luego, el usuario debe ingresar una opción (1, 2 o 3) y el
programa debe mostrar un mensaje según su elección:
● Si elige 1 → “Mostrando datos...”
● Si elige 2 → “Modificando datos...”
● Si elige 3 → “Saliendo del sistema...”
● Si elige otra cosa → “Opción inválida”"""

def imprimir_menu():
    print("Ver datos")
    print("Modificar datos")
    print("Salir")
    print("Opción inválida")
imprimir_menu()                   
opcion = int(input("Ingrese una opción del 1 al 3"))

if opcion == 1: 
    print(f"Mostrando datos ... ,{imprimir_menu(opcion)}") 
elif opcion == 2:
    print(f"Modificando datos ..., {imprimir_menu(opcion)}")
elif opcion ==3:
    print(f"Saliendo del sistema ..., {imprimir_menu(opcion)}")
else:
    print("Opción Inválida") 

