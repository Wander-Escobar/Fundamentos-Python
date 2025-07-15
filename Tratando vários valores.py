print('Tratando vários valores')
print('=-'*15)

soma = 0
contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))

    if num != 999:
        contador += 1
        soma += num
    else:
        break
print(f'\nVocê digitou {contador} números e a soma entre eles foi {soma}')

