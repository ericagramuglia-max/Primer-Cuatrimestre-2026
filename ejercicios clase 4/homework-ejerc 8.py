"""Ejercicio N°8
Calculas precio final del envío
Una empresa de transporte ofrece su servicio para enviar paquetes a tres provincias de la Patagonia Argentina. 
Cuando un cliente quiere enviar un paquete, puede elegir por distintos tipos de pesos Ej: (paquete de 15 kg a 20 kg).
El cliente contrata el servicio de transporte eligiendo una provincia como destino y un peso de paquete. 
Se necesita realizar un algoritmo para saber el precio final a pagar. 
En la siguiente tabla se muestran los destinos con cada peso admitido y su precio correspondiente.
"""
provincia = input("Ingresar la provincia de destino (Santa Cruz, Chubut, Río Negro): ").lower()
peso = float(input("Ingrese el peso del paquete: "))
precio = 0
if provincia == "santa cruz":
    if peso >= 0 and peso <= 5: 
        precio = 200
    elif peso >= 6 and peso <= 10:
        precio = 300
    elif peso >=11 and peso<=20:
        precio = 400
        
elif provincia == "chubut":
    if peso >= 0 and peso <= 10: 
        precio = 350
    elif peso >= 11 and peso <= 15:
        precio = 390
    elif peso >=16 and peso<=25:
        precio = 420       
elif provincia == "rio negro":
    if  peso >= 0 and peso <= 12:
        precio = 400
    elif peso >= 13 and peso <= 18:
        precio = 480
    elif peso >=19 and peso<=26:
        precio = 510
else:
    print ("Provincia no válida")

if precio > 0: 
    print("El precio final a pagar es: ", precio)