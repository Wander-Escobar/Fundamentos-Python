print('Somador de números pares\n')

soma = 0
for cont in range(1,6):
    num = int(input(f'Digite o {cont}º número: '))
    
    if num % 2 == 0:
        soma += num

if soma == 0:
    print('Todos os números informados são  ÍMPARES !')
else:
    print(f'A soma de todos os números pares é {soma}.')