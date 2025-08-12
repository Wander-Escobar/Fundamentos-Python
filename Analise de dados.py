maior18 = homens = mulher_20_menos = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = input('Idade: ')

    while True:
        if idade.isdigit():
            idade=int(idade)
            break
        else:
            idade = input('Opção inválida! informe a idade: ')
    
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]

    while True:

        if sexo not in ('MF'):
            sexo = str(input('Opção inválida, informe o sexo: [M/F]  ')).upper()
        else:
            break

    print('-'*20)

    
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20_menos += 1

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    while True:
        if continuar not in ('SN'):
            continuar = str(input('Opção inválida, deseja continuar? [S/N] ')).upper().strip()
        else:
            break
    if continuar == 'N':
        break
    

print('-'*20)
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher_20_menos} mulher com menos de 20 anos')

