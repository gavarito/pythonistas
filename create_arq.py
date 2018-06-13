#!/usr/bin/python3
# Scrip Python para automação de tarefas:
# Funcionalidade Criar arquivo adicionando shebang
# e dando permisão de execucao ./

from subprocess import run

for x in range(1, 19):
    name = 'exercicio_{}.py'.format(x)
    try:
        with open(name, 'r') as arquivo:
            conteudo = arquivo.readlines()
            conteudo.insert(0, '#!/usr/bin/python3\n')
        with open(name, 'w+') as arquivo:
            for x in conteudo:
                arquivo.write(x)

    except FileNotFoundError:
        with open(name, 'a') as arquivo:
            arquivo.write('#!/usr/bin/python3\n')

    run(['sudo', 'chmod', '+x', name])
