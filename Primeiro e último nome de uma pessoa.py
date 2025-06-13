print('Primeiro e último nome de uma pessoa')
print()

nome = str(input('Digite seu nome completo: '))
separa = nome.split()

print('Seu primeiro nome é: {}'.format(separa[0]))
print('Seu último nome é: {}'.format(separa[-1]))