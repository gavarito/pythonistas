#!/usr/bin/python3
'''Faça um Programa que peça a temperatura em graus Farenheit,
 transforme e mostre a temperatura em graus Celsius.

    C = (5 * (F-32) / 9). '''

faren = float(input('Digite os graus Farenheit: '))
ceus = (5 * (faren-32)/9)
print('{:.0f}ºF é igual há {:.0f}ºC'.format(faren, ceus))
