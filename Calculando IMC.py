print('Calculadora de IMC\n')

peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))

IMC = peso / altura ** 2

if IMC < 18.5:
    print(f'\nSeu IMC é {IMC:.2f}. Você está abaixo do peso.')
elif IMC >= 18.5 and IMC < 25:
    print(f'\nSeu IMC é {IMC:.2f}. Você está com peso normal.')
elif IMC >= 25 and IMC < 30:
    print(f'\nSeu IMC é {IMC:.2f}. Você está com sobrepeso.')
else:
    print(f'\nSeu IMC é {IMC:.2f}. Você está com obesidade.')