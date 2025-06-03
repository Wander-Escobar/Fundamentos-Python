print('#'*28)
print('### Calculadora de notas ###')
print('#'*28)
print()

#repetição de script
while True:

    #repetição de nota n1
    while True:
        try:
            nota1 = float(input('Digite a primeira nota : '))
            print()
            break
                
        except ValueError:
            print('Nota inválida, verifique e digite novamente')
            print()
            
            
    #repetição de nota n2
    while True:
        try:
            nota2 = float(input('Digite a segunda nota : '))
            print()
            break
        except ValueError:
            print('Nota inválida, verifique e digite novamente')
            print()
            
                
    media = (nota1 + nota2)/2

    print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, media))
    print()

    
    repete = input('Deseja realizar outro calculo ? (s/n): ')
    print()

    #verificador de resposta válida
    while True:

        if repete in ('s','n'):
            print('Certo, vamos continuar! ')
            print()
            break
            
        else:
            print ('Opção inválida! Responda apenas com "s" ou "n". ')
            print()
                    
        
    #encerramento de script
    if repete == 'n':
        print('Calculadora encerrada.')
        print()
        break



            
    