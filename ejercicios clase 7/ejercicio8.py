"""FOR
8. Pedir 5 nombres y saludarlos
Situación: El programa debe pedirle al usuario que ingrese 5 nombres, uno por uno, y saludar a cada
persona con un mensaje personalizado como “Hola,[nombre]!”."""



for i in range(1,6,1):
    nombre = input("Ingrese su nombre: ")
    print("Hola, ", nombre, "!!!")
print("Fin del ciclo For")