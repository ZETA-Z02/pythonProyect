#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 10:34:44 2023

@author: zeta
"""

entrada = input("Ingrese una cadena de texto: ")
#elimina o mejor dicho remplaza los espacios por ningun espacio
entradaSin = entrada.replace(" ","")

#print(entradaSin)
#print(type(entradaSin))

# Carácter para separar la cadena
caracter_separador = '+'
caracter_separadorR = '-'

# Usar el método split() para dividir la cadena
partes = entradaSin.split(caracter_separador)
#print(partes)

# Mostrar las partes separadas
print("Partes separadas:")
for parte in partes:
    print("separando suma: ",parte)
    if type(parte)==list:
        partesResta = parte.split(caracter_separadorR)
    
for parte1 in partesResta:
    print("separando resta: ",parte1)

