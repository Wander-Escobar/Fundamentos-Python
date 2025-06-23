from datetime import date

print('Alistamento militar\n')

atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento ? '))
result = atual - nasc

if result < 18:
    print(f'\nInfelizmente você ainda nao pode se alistar !\nAinda faltam {18-result} anos.')
else:
    print(f'\nParabéns! Você tem {result} anos e já pode se alistar!!')
