print('Conversor de temperatura')
print()

while True:
    c = input('Informe a temperatura em ºC: ')
    print()

    try:
        c = float(c)
        break
    except ValueError:
        print('Valor inválido, tente novamente.')
        continue

F = (c*9/5)+32

print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF .'.format(c,F))