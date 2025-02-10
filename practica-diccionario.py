"""
  --------------------------
//EJERCICIOS DE DICCIONARIOS//
  --------------------------
"""

"""
#combina 2 listas y transformalas en un diccionario

nombres = ["Pedro", "Ana", "Luis"]
edades = [30, 25, 28]

diccionario = dict(zip(nombres, edades))
print(diccionario)
"""

"""
#dada una lista de elementos, crea un diccionario donde las 'keys' sean los valores de la lisa y los 'values' sean la cantidad de veces que el elemento aparece en la lista

def contar_frecuencia(lista):
    frecuencia = {}
    for palabra in lista:
        if palabra in frecuencia:
            frecuencia[palabra] +=1
        else:
            frecuencia[palabra] = 1
    return frecuencia

entrada = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]
print(contar_frecuencia(entrada))
"""

"""
#suma los valores de un diccionario

productos = {"manzana": 2, "banana": 3, "naranja": 1}
print(sum(productos.values()))
"""