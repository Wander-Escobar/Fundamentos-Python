print('Sorteio de alunos em lista')
print()

import random

while True:

    aluno1 = input('Digite o nome do primeiro aluno: ')
    aluno2 = input('Digite o nome do segundo aluno: ')
    aluno3 = input('Digite o nome do terceiro aluno: ')
    aluno4 = input('Digite o nome do quarto aluno: ')
    print()

    try:
        aluno1 = str(aluno1)
        aluno2 = str(aluno2)
        aluno3 = str(aluno3)
        aluno4 = str(aluno4)
        break
    except ValueError:
        print('Erro. Nome inválido detectado, tente novamente.')
        print()
        continue

lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)

print('O aluno escolhido foi {}.'.format(sorteado))