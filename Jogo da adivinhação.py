import random

print('Jogo da adivinhação')
print()

while True:

    while True:

        print()
        escolha = input('Digite um número de 1 a 5: ').strip()
        print()
        print('Você escolheu {}.'.format(escolha))

        try:
            escolha = int(escolha)
            
            if escolha not in (1,2,3,4,5):
                print('Escolha inválida!')
                continue
            break
        except ValueError:
            print('Escolha inválida!')
            continue

    lista = [1,2,3,4,5]

    computador = random.choice(lista)
    print('O computador escolheu {}'.format(computador))
    print()

    if computador == escolha:
        print('Parabéns, você acertou o número !')
    else:
        print('Que pena, você errou! tente novamente.')
        print()

    while True:
        again = input('Deseja jogar novamente? (s/n)')

        if again not in ('s','n'):
            print('Opção inválida ! Digite "s" ou "n".')
            print()
            continue
        break
    
    if again == 's':
        continue
    break

    

