from math import sqrt

print("hola usuario esta es una calculadora")

print('ingrese el tipo de operacion quiere hacer: 1=SUMA; 2=RESTA; 3=MULTIPLICACION; 4=DIVISION')

def suma(a,b):
    resultado = a + b
    return resultado
    
def resta(a,b):
    resultado = a - b
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division(a,b):
    resultado = a / b
    return resultado

def numeros():
    a = int(input("primer numero"))
    b = int(input("segundo numero"))
    return a,b


status = True
while status == True:
    respuesta = int(input("ingrese el numero de operacion: "))
  
    if respuesta == 1:
        numeros1 = numeros()
        resultadoOperacion = suma(numeros1[0],numeros1[1])
        print('el resultado es: ',resultadoOperacion)
    elif respuesta == 2:
        numeros1 = numeros()
        resultadoOperacion = resta(numeros1[0],numeros1[1])
        print('el resultado es: ',resultadoOperacion)
      
    elif respuesta == 3:
        numeros1 = numeros()
        resultadoOperacion = multiplicacion(numeros1[0],numeros1[1])
        print('el resultado es: ',resultadoOperacion)
      
    elif respuesta == 4:
        numeros1 = numeros()
        resultadoOperacion = division(numeros1[0],numeros1[1])
        print('el resultado es: ',resultadoOperacion)
      
    salir = input("desea salir: si/no")
  
    if salir == 'si' or salir == 's':
        status = False





