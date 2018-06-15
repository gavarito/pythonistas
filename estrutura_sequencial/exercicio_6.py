#!/usr/bin/python3
from math import pi
'''Faça um Programa que peça o raio de um círculo, 
calcule e mostre sua área '''

raio = float(input('Digite um raio de um circulo: '))
area = pi * (raio ** 2)
print("A area do circulo é igual há {:.2f}".format(area))
