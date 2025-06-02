print('################################################')
print('### Calculadora de sucessores e antecessores ###')
print('################################################')
print()
print()


while True :

    try:
        num = int(input('Digite um número: '))
        print()
        print('Voce digitou o numero ', num)


        suc = num + 1
        ant = num - 1

        print()
        print('O sucessor de {} é {}.'.format(num, suc))
        print('O antecessor de {} é {}.'.format(num, ant))
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
    
            
        

    except ValueError:
        print('Valor inválido! Digite um numero inteiro!')

        
