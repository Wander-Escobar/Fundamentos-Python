print('Conversor de bases numéricas\n')

print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL')

while True:
    opcao = (input('Escolha uma opção: '))

    try:
        opcao = int(opcao)
        if opcao not in (1,2,3):
            print('Opção inválida! Digite a opção escolhida novamente: ')
        break
    except ValueError:
        print('Opção inválida! Digite a opção escolhida novamente: ')

match(opcao):
    case 1:
        num = int(input('Digite um número a se convertido para binário: '))
        print(f'O numero {num} em binário é : {bin(num)[2:]} !')
    case 2:
        num = int(input('Digite um número a se convertido para octal: '))
        print(f'O numero {num} em octal é : {oct(num)[2:]} !')
    case 3:
        num = int(input('Digite um número a se convertido para hexadecimal: '))
        print(f'O numero {num} em hexadecimal é : {hex(num)[2:]} !')
