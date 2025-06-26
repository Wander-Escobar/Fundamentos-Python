print('Contador de pares\n')

numero = int(input('Até quanto deseja contar? '))

for cont in range(2,numero+1,2):
    print(f'{cont} ', end=' ')
print('Acabou !!!')