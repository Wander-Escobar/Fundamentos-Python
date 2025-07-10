print('Cálculo de fatorial\n')

numero = int(input('Digite um número para calcular o fatorial: '))

print(f'Calculando {numero}! : ', end = '')
fatorial = 1

for c in range (numero,0,-1):
    if c == 1:
        print(f'{c} ', end = '')
        fatorial *= c
    else:
        print(f'{c} x ', end = '')
        fatorial *= c

    

print(f'= {fatorial}')
