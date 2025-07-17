print('Criando tabela com valores aleatorios\n')

from random import randint

max = 5
tabela = []

for i in range(max):
    linha = []
    for j in range(max):
        valor = randint(1,50)
        linha.append(valor)
    tabela.append(linha)

print('\nTabela original: ')
for linha in tabela:
    print(' | '.join(f'{valor:^3}' for valor in linha))
