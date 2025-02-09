"""
 -----------------
//MANEJO DE LISTAS//
 -----------------
"""

"""
#se acceden a las listas desde 0 a n-1 siendo n el tamaño de la lista el numero especifico al que quieres acceder debe estar entre [] si pones valores negativos se imprimira desde el final al inicio
mi_lista = ["hola", "mundo", "como", "estas"]
print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])
print(mi_lista[3])
print(mi_lista[-1])
"""

"""
#para cambiar un elemento dentro de una lista vasta con especificar el elemento que se desea modificar poner '=' y el valor al que deseas cambiar
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista[0] = 1234
print(mi_lista)
"""

"""
#para eliminar un elemento dentro de una lista se usa del y se especifica el elemento de la lista a cambiar
mi_lista = ["hola", "mundo", "como", "estas"]
del mi_lista[1]
print(mi_lista)
"""

"""
#las listas pueden contener otras listas (listas anidadas) y se pueden acceder a cada uno de ellos como vimos antes
mi_lista = [[1, 2, 3], ["hola", ["practicando", "python"]]]
print(mi_lista[0][0])
print(mi_lista[1])
print(mi_lista[1][1][1])
"""

"""
#se pueden crear listas mas pequeñas desde una lista mas grande, para hacer eso se especifica un rango entre valores y un ':' entre los numeros especificados del ranto 'no se pueden poner numeros negativos ni empezar con un numero mayor y terminar con un numero menor
mi_lista = [1, 2, 3, 4, 5, 6, 7]
print(mi_lista[0:2])
print(mi_lista[0:5])
print(mi_lista[5:1])
"""

"""
#con la tecnica que vimos antes podemos modificar varios elementos a la vez especificando el rango dentro de la lista que queremos obtener e igualarlo (=) con los datos que queremos cambiar
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista[0:2] = [0, 1, 2]
print(mi_lista)
"""

"""
#se puede usar el operador + junto con el = para agregar nuevos elementos dentro de la lista
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista += [1, 2, 3]
print(mi_lista)
"""

"""
#podemos asignar a variables el contenido que estan en una lista pero la cantidad de variables debe ser igual a la canidad de elementos dentro de la lista
mi_lista = ["hola", "mundo", "como", "estas"]
x, y, z, q = mi_lista
x, y, z = mi_lista
print(x, y, z, q)
"""

"""
#para iterar una lista usamos el bucle for, dandole a una variable el valor actual del elemento de la lista que se ira actualizando por cada vuelta del bucle
mi_lista = ["hola", "mundo", "como", "estas"]
for l in mi_lista:
  print(l)
"""

"""
#si necesitamos tener un indice del elemento exacto en el que nos encontramos se puede hacer de la siguiente manera; tambien se puede personalizar de formas distintas
mi_lista = ["hola", "mundo", "como", "estas"]
for index, l in enumerate(mi_lista):
  print(index, l)
  print(f"{index}. {l}")
"""

"""
#si tenemos 2 listas diferentes que tenemos que iterar a la vez lo podemos hacer con 'zip'
mi_lista = ["hola", "mundo", "como", "estas"]
mi_otra_lista = [0, 5, 9, 7]
for l1, l2 in zip(mi_lista, mi_otra_lista):
  print(l1, l2)
"""

"""
  -----------------------
//METODOS PARA LAS LISTAS//
 ------------------------
"""

"""
#si queremos agregar elementos al final de la lista podemos usar el metodo append
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista.append(1234)
print(mi_lista)
"""

"""
#podemos fusionar listas con el metodo 'extend' y pasandole los valores que queremos agregar o con el nombre de la otra lista
mi_lista = ["hola", "mundo"]
mi_otra_lista = ["como", "estas"]
mi_lista.extend([1, 2])
print(mi_lista)
mi_lista.extend(mi_otra_lista)
print(mi_lista)
mi_lista.extend(mi_lista)
print(mi_lista)
"""

"""
#si queremos agregar nuevos elementos en un lugar especifico de una lista podemos usar el metodo insert que necesita primero el lugar donde quieres agregar un nuevo elemento y luego el elemento que quieres agregar 'separados por una ,'
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista.insert(2, "jelou")
print(mi_lista)
"""

"""
#si queremos eliminar un elemento de una lista usamos el metodo 'remove' y especificamos que elemeneto queremos que elimine, no toma indices
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista.remove("como")
print(mi_lista)
mi_lista.remove(1)
print(mi_lista)
"""

"""
#elimina el ultimo elemento de la lista, le puede pasar un indice para que elimine especificamente el objeto que se encuentra en ese indice; la diferencia con remove es que remove elimina el primer elemento con la coincidendcia del elemento (si es que pasamos el nombre del objeto dentro del parentesis de remove)
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista.pop()
print(mi_lista)
mi_lista.pop(1)
print(mi_lista)
"""

"""
#el metodo reverse invierte el orden de la lista, tambien se puede usar [::-1] para invertir la lista
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista.reverse()
print(mi_lista)
mi_lista[::-1]
print(mi_lista)
"""

"""
#el metodo sort ordena la lista de menor a mayor o de mayor a menor con el parametro 'reverse=True' y si la lista tiene palabras entonces las ordena por orden alfabetico
mi_lista = [7, 9, 5, 0, 2, 15, 869]
mi_lista.sort()
print(mi_lista)
mi_lista.sort(reverse=True)
print(mi_lista)
mi_otra_lista = ["hola", "mundo", "como", "estas"]
mi_otra_lista.sort()
print(mi_otra_lista)
"""

"""
#si quieres saber el index de un objeto que sabes que esta dentro de una lista puedes usar el metodo index y pasrle el objeto como parametro; tambien podemos buscar un elemento especificando que se omita cierta cantidad de elementos
mi_lista = ["hola", "mundo", "como", "estas"]
print(mi_lista.index("como"))
print(mi_lista.index("como", 1))
"""

"""
#el metodo clear elimina todos los elementos de una lista
mi_lista = ["hola", "mundo", "como", "estas"]
mi_lista.clear()
print(mi_lista)
"""

"""
#el metodo 'copy' copia todos los elementos de una lista
mi_lista = ["hola", "mundo", "como", "estas"]
nueva_lista = mi_lista.copy()
print(nueva_lista)
"""

"""
  -------------------
//LIST COMPPREHENSION//
  -------------------
"""
# es una forma avanzada de crear listas con menos codigo y mayor legibilidad

"""
#esta lista agrega numeros del 1 al 5 y los eleva al cuadrado
mi_lista = [x**2 for x in range(1, 6)]
print(mi_lista)
#el codigo de arriba reemplaza el codigo de abajo
mi_lista = []
for x in range (1, 6):
  mi_lista.append(x**2)
"""

# PUEDES AGREGAR CONDICIONALES EN LAS LIST COMPREHESION

"""
# esta lista agrega solo numeros pares en un rango de 1 a 11
mi_lista = [x for x in range(1, 11) if x % 2 == 0]
print(mi_lista)
# el codigo de arriba reemplaza:
mi_lista = []
for x in range(1, 11):
  if x % 2 == 0:
    mi_lista.append(x)
"""

"""
#esta lista agrega numeros pares y reemplaza los numeros impares por la palabra 'impar'
mi_lista = [x if x % 2 == 0 else "impar" for x in range(1, 10)]
print(mi_lista)
#el codigo de arriba reemplaza:
mi_lista = []
for x in range(1, 10):
  if x % 2 == 0:
    mi_lista.append(x)
  else:
    mi_lista.append("impar")
"""

#SE PUEDE USAR MULTIPLES BUCLES EN LAS LIST COMPREHESION

"""
#esta lista agrega pares (x, y) donde 'x' acepta valores del 1 al 3 y donde 'y' acepta cada letra del texto
mi_lista = [(x, y) for x in range(1, 4) for y in "abc"]
print(mi_lista)
#el codigo de arriba reemplaza:
mi_lista = []
for x in range(1, 4):
  for y in "abc":
    mi_lista.append((x, y))
"""

#PUEDES LLAMAR FUNCIONES DENTRO DE LAS LIST COMPREHESION

"""
#la segunda lista obtiene los elementos de la primera lista y reemplaza cada letra por sus mayusculas
nombres = ["jose", "juan", "ana", "alison"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)
#el codigo de arriba reemplaza:
nombres = ["jose", "juan", "ana", "alison"]
mayusculas = []
for nombre in nombres:
  mayusculas.append(nombre.upper())
"""

#SE PUEDE COMBINAR 2 LIStas EN UNA USANDO METODOS Y TAMBIEN SE PUEDEN ENUMERARLAS

"""
#la lista 'combinacion' agrega pares (edad, valor) como elementos de su lista
nombres = ["jose", "juan", "ana", "alison"]
edades = [23, 32, 21, 19]
combinacion = [(nombre, edad) for nombre,edad in zip(nombres, edades)]
print(combinacion)
"""

"""
#la lista enumerar agrega elementos en pares (i, nombre) donde 'i' enumara la posicion del elemento en la lista y 'nombre' obtiene los elementos de la lista anterior
nombres = ["jose", "juan", "ana", "alison"]
enumerar = [(i, nombre) for i, nombre in enumerate(nombres)]
print(enumerar)
"""