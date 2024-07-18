#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:55:45 2023

@author: zeta
"""

entrada = input("imgrese la operacion que desea hacer: ")

respuesta = eval(entrada)

print(respuesta)
print(type(respuesta))

print(entrada)
print(type(entrada))

#SEPARADOR DE DATOS PARA LAS OPERACIONES
# Obtener la entrada del usuario
entrada = input("Ingrese una cadena de texto: ")

entradaSin = entrada.replace(" ","")
# Carácter para separar la cadena
caracter_separador = '+'

# Usar el método split() para dividir la cadena
partes = entradaSin.split(caracter_separador)

# Mostrar las partes separadas
print("Partes separadas:")
for parte in partes:
    print(parte)

