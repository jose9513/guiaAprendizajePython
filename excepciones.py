"""
  --------------------
||Manejo de exepciones||
  --------------------  
"""

# para usar las excepciones se utiliza (try, except y finaly)
# ejem:

"""try:
    numero = int(input("ingrese un numero: "))
    resultado = 10/numero
    print(f"el resultado de la division es: {resultado}")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("ingrese solo numeros por favor")
finally:
    print("este es el fin del programa")"""
    
    
# Puedes definir tus propias excepciones usando la palabra clave (raise):

"""try:
    edad = int(input("ingrese su edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print(f"tienes {edad} años")
except ValueError as e:
    print(f"Error: {e}")"""
    
"""while True:
    try:
        numero = int(input("ingrese un numero entero: "))
        if numero % 2 != 0:
            raise ValueError("el numero debe ser par")
        else:
            print(f"el numero que ingreso es: {numero}")
            break
    except ValueError as e:
        print(e)"""
        
def sumar():
    """manejo de exvepciones simple con ValueError"""
    try:
        numero1 = int(input("ingrese un numero: "))
        numero2 = int(input("ahora ingrese otro numero: "))
        suma = numero1 + numero2
        print(suma)
    except ValueError:
        print("porfavor ingrese solo numeros")
        
def raiz():
    """manejo de excepciones para la raiz de un numero que se pide al usuario"""
    try:
        numero = int(input("ingrese un numero para hallar la raiz cuadrada: "))
        raiz = numero ** 0.5
        if numero < 0:
            raise ValueError("el numero no puede ser negativo")
        elif numero % 2 != 0:
            raise ValueError("el numero no puede ser impar")
        else:
            print(raiz)
    except ValueError:
        print("ingrese solo numeros por favor")
        
"""lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("ingrese el indice dentro de la lista: "))
    print(f"el elemento en el indice {indice} es {lista[indice]}")
except ValueError:
    print("por favor solo ingrese solo numero por favor")
except IndexError:
    print("el indice ingresado no existe dentro de la lista")"""