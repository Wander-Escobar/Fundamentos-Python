print('Calculadora de desconto')
print()

while True:

    preço = input('Qual é o preço do produto? R$')
    print()
    
    try:
        preço = float(preço)
        break
    except ValueError:
        print('')

result = preço - (preço * 5 / 100)

print(' O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preço,result))