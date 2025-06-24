print('Classificando atletas por idade\n')

from datetime import date

atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = atual - nascimento

if idade <= 9:
    print(f'\nO atleta possui {idade} anos e está classificado como MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'\nO atleta possui {idade} anos e está classificado como INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'\nO atleta possui {idade} anos e está classificado como JUNIOR!')
elif idade > 19 and idade <= 25:
    print(f'\nO atleta possui {idade} anos e está classificado como SÊNIOR!')
else:
    print(f'\nO atleta possui {idade} anos e está classificado como MASTER!')