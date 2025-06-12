print('Separador de digitos de um número')
print()

numero = int(input('Informe um número: '))
print('Analisando o numero: ', numero)
print()

un = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print('Unidade: ',un)
print('Dezena: ', dez)
print('Centena: ',cen)
print('Milhar: ',mil)
print()

print('Separação finalizada.')
