print('Calculadora')

while True:
    print('-'*15)
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*15)

    if valor < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!!!')
    else:          
        for cont in range (1,11):
            print(f'{valor} x {cont} = {valor*cont}')