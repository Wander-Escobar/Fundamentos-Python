print('Sequencia de Fibonacci')
print('='*15)

numero_um = 1
numero_dois = 1
soma = 0

total = int(input('Quantos numeros da sequência deseja visualizar? '))

if total < 2:
    print('Quantidade inválida! A sequência precisa de pelo menos 2 números.')

else:
    print(f'{numero_um} + {numero_dois}', end = '')
    print(' -> FIM ! ' if total == 2 else ' + ',end = '')
    total -= 2

    while total != 0: 
        print(f'{numero_um+numero_dois}', end = '')
        print(' + ' if total != 1 else ' -> FIM ! ',end = '')
        soma = numero_um + numero_dois
        numero_um = numero_dois
        numero_dois = soma
                
        total -= 1
