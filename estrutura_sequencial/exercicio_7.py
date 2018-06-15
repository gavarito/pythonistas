#!/usr/bin/python3
'''Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário.'''

lado = float(input('Digite o valor de um lado do quadrado: '))
area = lado * lado
area_dobro = area * 2
print("O dobro da area do quadradro é igual há {}".format(area_dobro))
