print('Qual pessoa é a mais leve ou pesada ?\n')

leve = 10**500
pesada = 0

for cont in range(1,6):
    peso = float(input(f'Qual o peso da {cont}ª pessoa? '))
    if peso < leve:
        leve = peso
    if peso > pesada:
        pesada = peso

print(f'\nO maior peso lido foi {pesada:.2f}kg')
print(f'O menor peso lido foi {leve:.2f}kg')