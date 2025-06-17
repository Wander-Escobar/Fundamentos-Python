print('Custo de viagem\n')

distancia = float(input('Qual a distancia até o destino desejado? '))

if distancia < 201:
    print(f'\nA viagem de {distancia:.2f}Km terá o custo de R${distancia*0.5:.2f} reais')
else:
    print(f'\nA viagem de {distancia:.2f}Km terá o custo de R${distancia*0.45:.2f} reais')