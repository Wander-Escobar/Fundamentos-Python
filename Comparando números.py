print('Comparando números, qual é maior ?\n')

while True:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')

    try:
        num1 = int(num1)
        num2 = int(num2)
        break
    except ValueError:
        print('\nOpção inválida! Digite novamente a opção desejada!')

if num1 < num2:    
    print('\nO SEGUNDO valor é maior')
if num1 > num2:
    print('\nO PRIMEIRO valor é maior ')
else:
    print('\nOs dois valores são IGUAIS\n')