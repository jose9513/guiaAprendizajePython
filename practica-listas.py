"""
  -------------------
//practica con listas//
  -------------------
"""
"""
#crear una lista que contenga los numeros impares del 1 al 20 con 'LIST COMPREHESION', luego crear otra lista que tome los numeros de la primera lista pero que sean menores a '15'

lista1 = [x for x in range(1, 20, 2)]
lista2 = [x for x in lista1 if x < 15]
print(lista2)
"""

"""
#crear una lista con nombres, luego crear otra lista que agregue los nombres de la primera lista solo si los nombres tienen mas de 5 letras

lista1 = ["jose", "leonardo", "alison", "yamile", "maria"]
lista2 = [x for x in lista1 if len(x) > 5]
print(lista2)
"""

"""
#crea una lista de numeros cualquiera, luego crea otra lista que agregue los numeros de la primera lista pero elevandolos al cuadrado

lista1 = [1, 5, 7, 9, 45, 23, 14, 69, 87, 16, 20]
lista2 = [x**2 for x in lista1]
print(lista2)
"""

"""
#dado un numero (mayor o igual a 10) crea una lista que devuelva el doble del numero y la suma de sus digitos

def lista(n):
    return[n * 2, sum(int(digito) for digito in str(n))]

print(lista(15))
"""

"""
#dada una lista de numeros enteros crea otra lista que agreguen los elementos de la primera lista solo si los elementos son pares y positivos

lista1 = [1, 9, 5, 6, 12, 45, 78, 32, 10, 5, 48, 79, 63, 52, 56, 40, 51, 52, 86, 97, 92, 23, -98, -12, -56, -45 -74]
lista2 = [x for x in lista1 if x % 2 == 0 and x > 0]
print(lista2)
"""

"""
#dada un alista de numeros enteros, crea otra lista con los elementos que cumplan con las siguientes condiciones: 1. el numero es mayor o igual a 10; 2. la suma de sus digitos es impar

lista1 = [42, 7, 56, 23, 91, 5, 38, 77, 16, 62, 84, 9, 14, 99, 45, 21, 70, 13, 35, 60, 88, 19, 33, 48, 72]
lista2 = [x for x in lista1 if x >= 10 and sum(int(digito) for digito in str(x)) % 2 != 0]
print(lista2)
"""

"""
#crea una funcion que reciba una lista de listas y devuelva la suma de todos los elementos internos que sean primos

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
        return n

def iteracion_listas(lista_iterable):
    total = 0
    for x in lista_iterable:
        for y in x:
            primo =es_primo(y)
            total += primo
    return total   
    
lista_de_listas = [
    [42, 7, 56, 23, 91],
    [5, 38, 77, 16, 62],
    [84, 9, 14, 99, 45],
    [21, 70, 13, 35, 60],
    [88, 19, 33, 48, 72]
]

print(iteracion_listas(lista_de_listas))
"""

"""
#crea una funcion que devuelva el segundo numero mas grande de una lista

def segundo_mayor(lista):
    lista.remove(max(lista))
    return max(lista)

mi_lista = [42, 7, 56, 23, 91, 5, 38, 77, 16, 62, 84, 9, 14, 99, 45, 21, 70, 13, 35, 60, 88, 19, 33, 48, 72]

print(max(mi_lista))
print(segundo_mayor(mi_lista))
"""

"""
#dada una lista con 'n' numeros crea una funcion que devuelva cuantos numeros son mayores que el numero especificado por el usaurio

def numeros_mayores(lista, n):
    return [x for x in lista if x > n]

mi_lista = [42, 7, 56, 23, 91, 5, 38, 77, 16, 62, 84, 9, 14, 99, 45, 21, 70, 13, 35, 60, 88, 19, 33, 48, 72]
print(numeros_mayores(mi_lista, 75))
"""

"""
#dada una lista de listas crea una nueva lista que obtenga los elementos de las sublistas con list comprehesion

def elementos_sublista(lista):
    nueva_lista = [elemento for sublista in lista for elemento in sublista]
    return nueva_lista
    
lista_de_listas = [
    [42, 7, 56, 23, 91],
    [5, 38, 77, 16, 62],
    [84, 9, 14, 99, 45],
    [21, 70, 13, 35, 60],
    [88, 19, 33, 48, 72]
]

print(elementos_sublista(lista_de_listas))
"""

"""
#dada una lista de listas invierte los elementos de las sublistas sin invertir las posiciones de las listas  

lista_de_listas = [
    [42, 7, 56, 23, 91],
    [5, 38, 77, 16, 62],
    [84, 9, 14, 99, 45],
    [21, 70, 13, 35, 60],
    [88, 19, 33, 48, 72]
]

nueva_lista = [sublista[::-1] for sublista in lista_de_listas]
print(nueva_lista)
"""

"""
#dada una lista de 'n' numeros, crea una funcion que rote los elementos 'n' numeros a la derecha

def rotar_derecha(lista, n):
    n = n % len(lista)
    return lista[-n:] + lista[:-n]

mi_lista = [42, 7, 56, 23, 91]

print(rotar_derecha(mi_lista, 3))
#NOTA: el '::' se usa para manipular una lista de la siguiente manera: inicio:fin:saltos; al 'inicio' se indica desde donde quieres iniciar a iterar la lsita, en el 'fin' es hasta donde quieres llegar, en los 'saltos' se especifica cuantos saltos quieres que de la iteracion (si das un valor de '1' se itera toda la lista de manera comun, si das el valor de '2' hara un salto eligioendo uno si y el siguiente no)
"""

"""
#dada una lista de enteros crea una nueva lista que reemplace los numeros negativos por '0'

mi_lista = [-34, 76, -29, 88, -12, 53, -47, -78, 95, -6, 32, -55, 27, -63, 18, -91, 46, 7, -24, 59, -38, -5, 81, -73, 14]

nueva_lista = [elemento if elemento > 0 else 0 for elemento in mi_lista]
print(nueva_lista)
"""

"""
#transforma una lista de strings a una lista de longitudes

mi_lista = ["hola", "mundo", "como", "estas"]

nueva_lista = [len(elemento) for elemento in mi_lista]
print(nueva_lista)
"""

"""
#dada una lista de 'n' numeros, divide la lista en 2 listas, una de pares y otra de impares


lista = [2, 7, 14, 23, 34, 45, 52, 61, 78, 89]

lista_pares = [x for x in lista if x % 2 == 0]
lista_impares = [y for y in lista if y % 2 != 0]
print(f"{lista_pares} \n {lista_impares}")
"""

"""
#encuentra los elementos comunes entre 2 listas

def elementos_iguales(lista1, lista2):
    iguales = []
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento2 == elemento1:
                iguales.append(elemento2)
                
    return iguales

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

print(elementos_iguales(lista1, lista2))

numeros_iguales = [elemento for elemento in lista1 for elemento2 in lista2 if elemento == elemento2]
print(numeros_iguales)
"""

"""
#dada una lista de numeros encuentra el segundo numero mas grande sin elminar ningun numero

lista = [2, 7, 14, 23, 34, 45, 52, 61, 78, 89]

def segundo_mas_grande(lista):
    mas_grande = max(lista)
    return max(i for i in lista if i <mas_grande)
    
print(segundo_mas_grande(lista))
"""

"""
#dada una lista de listas, ordena las sublistas segun la suma de sus elementos

lista_de_listas = [
    [42, 7, 56, 23, 91],
    [5, 38, 77, 16, 62],
    [84, 9, 14, 99, 45],
    [21, 70, 13, 35, 60],
    [88, 19, 33, 48, 72]
]

lista_ordenada = sorted(lista_de_listas, key=sum)
print(lista_ordenada)
"""

"""
#dada 2 listas, crea una nueva lista alternando los elementos de las 2 listas anteriores

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]

nueva_lista = [elemento for par in zip(lista1, lista2) for elemento in par]
print(nueva_lista)
"""