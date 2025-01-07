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
    
while True:
    try:
        numero = int(input("ingrese un numero entero: "))
        if numero % 2 != 0:
            raise ValueError("el numero debe ser par")
        else:
            print(f"el numero que ingreso es: {numero}")
            break
    except ValueError as e:
        print(e)