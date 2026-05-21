
"""Listas unidimensionales"""
"""

mi_vector = ["azul", "rojo", "verde"]
print(mi_vector[1])  
print (type(mi_vector[1]))

"""

"""Análisis de un vector de temperaturas

Tenes registrado este vector con temperaturas de 5 días:

temperaturas = [23, 28, 21, 25, 30]
"""print("Primer dia ", temperaturas[0])
print("último día ", temperaturas[4])
temperaturas[3] = 40         """                #    cambio el dato de la posición 3"""

#Tenes registrado este vector con temperaturas de 5 días:
 
temperaturas = [23, 28, 21, 25, 30]
 
"""Completa el siguiente código para acceder a
la primera y última temperatura registrada:"""
 
"""print("Primer día: ",temperaturas[0])
print("Último día: ",temperaturas[4])"""
 
"""temperaturas[3]=40
 
print(temperaturas)
 
for i in temperaturas:
    print(i)
    if i == 25:
        break
print("el 25 fue encontrado")"""




 #listas multidimensionales
cubo = [[[1,2],[3,4]],[[5,6],[7,8]]]
#             0             1
#          0     1       0     1
#         0 1   0 1     0 1   0 1
print(cubo[0][1][0])
