from random import shuffle

print('Sorteando uma ordem na lista')
print()

aluno1 = str(input('Digite o nome do primreiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
aluno5 = str(input('Digite o nome do quinto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4, aluno5]

shuffle(lista)

print()
print('A ordem de apresentação será: ')
print(lista)