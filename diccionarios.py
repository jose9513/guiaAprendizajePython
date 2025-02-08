"""
  ------------------------
//CREACION DE DICCIONARIOS//
  ------------------------
"""

"""
#los diccionarios son una opcion para manejar datos que se dividen en pares 'key:value' separados por comas
mi_diccionario = {
    "nombre" : "Jose",
    "edad" : 23,
    "nacionalidad" : "Peruano"
}
print(mi_diccionario)
"""

"""
#otra forma de crear diccionarios es con 'dict' y hay diferenes formas de usar dict
mi_diccionario = dict([
    ("nombre", "Jose"),
    ("edad", 23),
    ("nacionalidad", "Peruano")
])
print(mi_diccionario)

mi_otro_diccionario = dict(nombre = "Jose",
                           edad = 23,
                           nacionalidad = "Peruano")
print(mi_otro_diccionario)
"""

"""
  -----------------------------------------------
//ACCEDER Y MODIFICAR ELEMENTOS EN UN DICCIONARIO//
  -----------------------------------------------
"""

"""
#se puede acceder a un elemento con '[]' o con el componente 'get'
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
print(mi_diccionario["nombre"])
print(mi_diccionario.get("edad"))
"""

"""
#puedes agregar elementos poniendo la 'key' entre '[]' e igualandolo con el valor que desees
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
mi_diccionario["calle"] = "calle123"
print(mi_diccionario.get("calle"))
"""

"""
  ---------------------------
//ITERACION EN UN DICCIONARIO//
  ---------------------------
"""

"""
#usamos el bucle for para iterar entre las diferentes 'keys' del diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
for x in mi_diccionario:
  print(x)
"""

"""
#usamos el bucle for para iterar entre los diferentes 'values' del diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
for x in mi_diccionario:
  print(mi_diccionario[x])
"""

"""
#tambien se pueden iterar entre las 'keys' y los 'value' a la misma vez
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
for x, y in mi_diccionario.items():
  print(x, y)
"""

"""
#tambien se pueden crear diferentes formas de imprimir las 'keys' junto con los 'values' del diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
for x, y in mi_diccionario.items():
  print(f"{x} : {y}")
"""

"""
  ---------------------
//DICCIONARIOS ANIDADOS//
  ---------------------
"""

"""
#aqui juntamos los diccionarios 'dic_1' con 'di_2' dentro del diccionario 'd'
dic_1 = {
  "numero" : 1,
  "letra" : "a"
}
dic_2 = {
  "numero" : 2,
  "letra" : "b"
}
d = {
  "anidado1" : dic_1,
  "anidado2" : dic_2
}
print(d)
"""

"""
  -------------------------
//METODOS PARA DICCIONARIOS//
  -------------------------
"""

"""
#el metodo 'clear' elimina todo el contenido que hay dentro de un diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
mi_diccionario.clear()
print(mi_diccionario)
"""

"""
#el metodo 'get' obtiene el value de la 'key' ingresada, no es necesario ingresar el segundo parametro pero en caso de ser ingresado se devolvera el segundo parametro aun que no exista en la lista
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
print(mi_diccionario.get("nombre"))
print(mi_diccionario.get("edad", 23))
print(mi_diccionario.get("direccion", "calle123"))
"""

"""
#el metodo 'items' devuelve los 'keys' y 'values' del diccionario, tambien se puede listar el diccionario con el metodo 'lit' como si fuera una lista
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
print(mi_diccionario.items())
it = mi_diccionario.items()
print(list(it))
print(list(it)[0][0])
"""

"""
#el metodo 'key' devuelve todas las keys de un diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
print(mi_diccionario.keys())
"""

"""
#el metodo 'values' devuelve todos los 'values' del diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
print(mi_diccionario.values())
"""

"""
#el metodo 'pop' elimina el valor ingresado que se encuentre en la lista, no es necesario poner el segundo valor, si se ingresa valores que no estan en un diccionario no saldria error y solo se devolveria la lista tal y como esta
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23
}
mi_diccionario.pop("nombre")
print(mi_diccionario)
mi_diccionario.pop("direccion", "calle123")
print(mi_diccionario)
"""

"""
#el metodo 'popitem' elimina un elemento aleatorio de un diccionario
mi_diccionario = {
  "nombre" : "jose",
  "edad" : 23,
  "direccion" : "calle123",
  "numero" : 1,
  "letra" : "a"
}
mi_diccionario.popitem()
print(mi_diccionario)
"""


#el metodo 'update' recibe como parametro otro diccionario y agrega los elementos que no esten en el primer diccionario
dic_1 = {
  "numero" : 1,
  "letra" : "a"
}
dic_2 = {
  "numero" : 2,
  "letra" : "b",
  "segundo_numero" : 1
}
dic_1.update(dic_2)
print(dic_1)
