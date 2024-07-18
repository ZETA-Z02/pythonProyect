from math import *

print('''BIENVENIDO :)
      ESTO ES UNA CALCULADORA USANDO CLASES''')
print('''INGRESE EL TIPO DE OPERACION QUE DESE HACER
1 = SUMA 
2 = RESTA 
3 = MULTIPLICACION
4 = DIVISION
5 = POTENCIA''')

class datos:
    def __init__(self,*arg,**kwargs):
        pass
        
def numeros():
    a = int(input("primer numero: "))
    b = int(input("segundo numero: "))
    return a,b

class calculador:
    def __init__(self,num1,num2):
        
        self.numero1 = num1
        self.numero2 = num2
    
    def sumar(self):
        return print(self.numero1+self.numero2)
    def restar(self):
        return print(self.numero1-self.numero2)
    def multiplicar(self):
        return print(self.numero1*self.numero2)
    def dividir(self):
        return print(self.numero1/self.numero2)
    def potenciar(self):
        return print(self.numero1**self.numero2)
    
while True:
    respuesta = int(input("ingrese el numero de operacion: "))
    numero = numeros()
    calculadora = calculador(numero[0],numero[1])
    # print(calculadora.numero2)
    if respuesta==1:
        calculadora.sumar()
    elif respuesta==2:
        calculadora.restar()
    elif respuesta==3:
        calculadora.multiplicar()
    elif respuesta==4:
        calculadora.dividir()
    elif respuesta==5:
        calculadora.potenciar()
        
    if input('desea salir: si/no: ')=='si':
        break
    
    