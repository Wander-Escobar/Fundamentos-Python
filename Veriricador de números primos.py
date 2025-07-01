print('Verificador de números primos\n')

from math import sqrt, trunc

primos = []
quantidade = 0


inicio = int(input('Informe o número de inicio: '))
fim = int(input('Informe o número do término: '))

for cont in range(inicio,fim+1):
    divisores = 0    
    for cont2 in range(1,trunc(sqrt(cont))+1):
        if cont % cont2 == 0:
            divisores += 1
            if cont2 != cont // cont2:
                divisores += 1
    if divisores == 2:
        primos.append(cont)
        quantidade += 1

print(f'No intervalo dos números {inicio} e {fim} há {quantidade} números primos.\n')

mostrar_primos = input('Deseja visualizar o números primos identificados ? (s/n): ').strip().lower()

if mostrar_primos not in ('s','n'):
    print('Opção inválida, escolha usando "s" ou "n".')
elif mostrar_primos == 's':
    print(primos)

