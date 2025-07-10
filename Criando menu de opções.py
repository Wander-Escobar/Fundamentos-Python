print('Criando menus com cálculos\n')

from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while True:
     
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n')

    opcao = int(input('Qual é a sua opção? '))

    match opcao:
        case 1:
            print(f'\nA soma entre {valor1} e {valor2} é {valor2+valor1}.\n')
        case 2:
            print(f'\nO produto da multiplicação e entre {valor1} e {valor2} é {valor2*valor1}.\n')
        case 3:
            if valor1 == valor2:
                print('\nOs dois números apresentados são iguais\n.')
            elif valor1 > valor2:
                print(f'\nO valor {valor1} é maior.\n')
            else:
                print(f'\nO valor {valor2} é maior.\n')
        case 4:
            print()
            valor1 = int(input('Primeiro valor: '))
            valor2 = int(input('Segundo valor: '))
            print()
            continue
        case 5:
            print('\nFinalizando programa', end = '',flush=True)
            sleep(1)
            print('.', end = '',flush=True)
            sleep(1)
            print('.', end = '',flush=True)
            sleep(1)
            print('.', end = '',flush=True)
            sleep(1)
            print('.',flush=True)
            print('Programa finalizado!')
            break

