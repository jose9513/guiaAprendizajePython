"""
  ------------------
//CREACION DE TUPLAS//
  ------------------
"""

"""
#las tuplas se crean entre parentesis
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
"""

"""
#las tuplas tambien se pueden declarar sin parentesis
mi_tupla = 1, 2, 3, 4, 5
print(type(mi_tupla))
print(mi_tupla)
"""

"""
  ----------------------
//OPERACIONES CON TUPLAS//
  ----------------------
"""

"""
#las tuplas no se pueden modificar, si intentas hacerlo te dara un error
mi_tupla = (1, 2, 3, 4, 5)
mi_tupla[0] = 5
"""

"""
#al igual que las listas las tuplas tambien pueden se anidadas
mi_tupla = (1, 2, 3, ("a", "b", "c"), 4, 5)
print(mi_tupla)
"""

"""
#es posible transformar una lista a tupla con 'tuple'
lista = [1, 2, 3, 4, 5]
mi_tupla = tuple(lista)
print(type(mi_tupla))
print(mi_tupla)
"""

"""
#tambien se puede iterar por cada elemento de la tupla como lo hacias con las listas
mi_tupla = (1, 2, 3, 4, 5)
for i in mi_tupla:
    print(i)
"""

"""
#se puede crear variables vacias y asignarles el valor de los elementos de la tupla
mi_tupla = (1, 2, 3, 4, 5)
a, b, c, d, e = mi_tupla
print(a, b, c, d, e)
"""



mi_tupla = (1,)
print(type(mi_tupla))
print(mi_tupla)
