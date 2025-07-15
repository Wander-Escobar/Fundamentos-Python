print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)

from random import randint
contador = 0

while True:

    valor = int(input('Digite um valor: '))
    while True:
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()
        if escolha not in 'PI':
            print('Opção inválida! Tente novamente.')
        else:
            break
    aleatorio = randint(1,2)
    resultado = (aleatorio+valor)%2
    print('-'*40)
    print(f'Você jogou {valor} e o computador {aleatorio}. total de {valor+aleatorio} ', end='')
    print('DEU PAR' if resultado == 0 else 'DEU ÍMPAR')
    print('-'*40)

    if resultado == 0 and escolha == 'P':
        print('Você GANHOU!!!\nVamos jogar novamente.....\n')
        contador += 1
    else:
        print(f'GAME OVER! Você venceu {contador} ', end ='')
        print('vez.' if contador == 1 else 'vezes.')
        break
 