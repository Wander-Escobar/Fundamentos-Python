print('Jogo da adivinhação v2.0\n')

from random import randint

computador = randint(1,10)
tentativas = 1

print('Acabei se pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
jogador = int(input('\nQual o seu palpite? '))

while jogador != computador:
    if jogador > computador:
        print('\nMenos... Tente novamente.')
        jogador = int(input('\nQual o seu palpite? '))
    else:
        print('\nMais... Tente novamente.')
        jogador = int(input('\nQual o seu palpite? '))
    tentativas += 1

print(f'Parabéns! Você acertou com {tentativas} tentativas.')
