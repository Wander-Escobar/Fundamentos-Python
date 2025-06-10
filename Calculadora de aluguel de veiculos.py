print('Aluguel de carros')
print()

while True:
    dias = input('Quantos dias alugados? ')
    km = input('Quantos km rodados? ')

    try: 
        dias = float(dias)        
        km = float(km)
        break
    except ValueError:
        print('Valor inválido! Tente novamente.')
        print()
        continue

custo = (dias * 60) + (km * 0.15)

print()
print('O total a pagar é de R${:.2f}'.format(custo))