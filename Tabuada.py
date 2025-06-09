
while True:
    numero = input('Digite um número para ver sua tabuada: ')
    print()
    
    if numero.isnumeric():
        numero = int(numero)
        break
    else:
        print('Opção invalida!')
        continue

cont = 1

while True:
    if cont < 11:
        result = int(numero * cont)
        print('{} x {:2} = {}'.format(numero,cont,result))
        cont = cont + 1
        continue
    break