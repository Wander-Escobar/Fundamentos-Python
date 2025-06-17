print('Verificador de ano bissexto\n')

ano = int(input('Informe um ano: '))

if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
    print(f'\nO ano {ano} é bissexto! ')
else:
    print(f'\nO ano {ano} NÃO é bissexto! ')