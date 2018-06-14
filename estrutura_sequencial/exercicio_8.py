#!/usr/bin/python3
'''Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês. '''

salario_hora = float(input("Quanto você ganha por hora?\nR$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês?\n"))
salario_mensal = salario_hora * horas_trabalhadas
print('Seu salario mensal é igual há: R${:.2f}'.format(salario_mensal))
