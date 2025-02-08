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
