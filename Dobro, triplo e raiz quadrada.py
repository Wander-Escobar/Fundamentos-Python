print('#'*54)
print('#### Calculadora de DOBRO, TRIPLO e RAIZ QUADRADA ####')
print('#'*54)
print()
print()

while True :

    try:

        num = int(input('Digite um numero para cálculo: '))
        print()
        
    except ValueError:
        print('Numero inválido, insira um numero do tipo inteiro!')
        continue
    
    dobro = num * 2
    triplo = num * 3
    raiz = num ** 0.5

    print('O dobro de {} é: {} '.format(num, dobro))
    print('O triplo de {} é: {} '.format(num, triplo))
    print('A raiz quadrada de {} é: {:.0f} '.format(num, raiz))
    print()

    while True:
        repete = input('Deseja realizar outro calculo ? (s/n): ').lower()
    
        if repete in ('s','n'):
            print('Você digitou: ', repete)
            break
        else:
            print()
            print('Opção inválida! Digite apenas "s" ou "n" !')
            print()
           
            
    if repete == 'n':
        break

    if repete == 's':
        print()
        print('Ok, vamos lá: ')
        print()   