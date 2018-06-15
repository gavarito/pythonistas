#!/usr/bin/python3
''' Faça um Programa que peça as 4 notas bimestrais e mostre a média. '''

# nota1 = float(input('digite a nota 1: '))
# nota2 = float(input('digite a nota 2: '))
# nota3 = float(input('digite a nota 3: '))
# nota4 = float(input('digite a nota 4: '))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print('A média é igual há {:.2f}'.format(media))

soma = 0
for x in range(4):
    nota = float(input('digite a nota {}: '.format(x+1)))
    soma += nota
print('A média é igual há {:.2f}'.format(soma/4))
