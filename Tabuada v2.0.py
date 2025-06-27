print('Reprodutor de tabuadas: \n')

tabuada = int(input('Informe a tabuada desejada: '))

for cont in range(1,11):
    print(f'{tabuada} x {cont:2} = {tabuada * cont}')