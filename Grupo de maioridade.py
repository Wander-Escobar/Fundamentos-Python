print('Verificador de maiores e menores de idade\n')

from datetime import date

atual = date.today().year
maior = 0
maiores = []
menor = 0
menores = []

for ano in range(1,8):
    nasc = int(input(f'Em que ano a {ano}ª pessoa nasceu? '))
    if atual-nasc >= 18:
        maior += 1
        maiores.append(nasc)
    else:
        menor += 1
        menores.append(nasc)

print(f'\nAo todo tivemos {maior} pessoas maiores de idade\nE também tivemos {menor} pessoas menores de idade')

mostrar_anos = str(input('\nDeseja visualizar o ano de nascimento dos maiores e menores de idade ? (S/N): ')).upper()

while True:
        
    if mostrar_anos not in ('S','N'):
        print('Opção inválida! Tente novamente usando "S" ou "N"!')
    elif mostrar_anos == 'N':
        break
    else:
        print('Maiores: ',maiores)
        print('Menores: ',menores)
        break

