print('Radar eletrônico ')
print()

velocidade = int(input('Informe a velocidade atual do veiculo: '))

if velocidade > 80:
    print(f'MULTADO!!! O limite de velocidade é de 80km/h')
    print(f'Sua velocidade é {velocidade} e ultrapassou em {velocidade -80}km/h do limite')
    print(f'Multa gerada no valor de R${(velocidade-80)*7}reais')
else:
    print('Limite de velocidade respeitado, continue assim!')