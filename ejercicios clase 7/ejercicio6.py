"""6. Ingreso de contraseña
Situación: El programa debe pedir al usuario que ingrese una contraseña.
Solo se permite acceder si la contraseña ingresada es "python123".
Si es incorrecta, debe pedirla nuevamente hasta que sea correcta.
Al ingresar la correcta, mostrar "Acceso autorizado"."""

contrasenia = input("Ingrese la contraseña: ")

while contrasenia != "python123":
       contrasenia = input("Ingresa la contraseña: ")
            
input("ACCESO AUTORIZADO")



