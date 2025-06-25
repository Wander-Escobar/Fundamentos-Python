import random

print('PEDRA, PAPEL OU TESOURA\n\nVamos jogar ?\n\nSuas opções:\n')
print('[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n')

while True:

    jogador = input('Qual é a sua jogada ? ').capitalize().strip()

    if jogador == '1':
        jogador = 'Pedra'
    elif jogador == '2':
        jogador = 'Papel'
    elif jogador == '3':
        jogador = 'Tesoura'

    jogadas_computador = ['pedra', 'papel', 'Tesoura']
    computador = random.choice(jogadas_computador)

    if jogador == 'Pedra' and computador == 'Tesoura':
        print(f'\nVocê escolheu {jogador} e o computador {computador}.')
        print('Você venceu !!!')
    elif jogador == 'papel' and computador == 'pedra':
        print(f'\nVocê escolheu {jogador} e o computador {computador}.')
        print('Você venceu !!!')
    elif jogador == 'tesoura' and computador == 'papel':
        print(f'\nVocê escolheu {jogador} e o computador {computador}.')
        print('Você venceu !!!')
    elif jogador == computador:
        print(f'\nVocê escolheu {jogador} e o computador {computador}.')
        print('EMPATE !!!')
    else:
        print(f'\nVocê escolheu {jogador} e o computador {computador}.')
        print('Você perdeu... =/')

    repetir = input('\nDeseja jogar novamente ? (s/n): ').lower().strip()
    if repetir != 's':
        break
