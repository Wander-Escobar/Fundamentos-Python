print('Media, menor e maior valor')
print('-='*15)

contador = 0
soma = 0
maior = None
menor = None

while True:
    valor = int(input('Digite um valor: '))
    soma += valor
    contador += 1
    if menor == None or menor > valor:
        menor = valor
    elif maior == None or maior < valor:
        maior = valor

    while True:
        continuar = str(input(f'Deseja continuar ? [S/N]')).strip().upper()
        if continuar not in ('S','N'):
            print('Opção inválida, tente novamente.')
        break
    if continuar == 'N':
        break

media = float(soma / contador)
print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')