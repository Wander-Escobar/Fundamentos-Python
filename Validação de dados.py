print('Validação de dados\n')

sexo = str(input('Informe seu sexo: [M/F]: ')).upper().strip()[0]

while True:
    if sexo not in ('M','F'):
        sexo = str(input('Opção inválida, por favor informe seu sexo: [M/F]: ')).upper().strip()[0]
    else:
        break
print(f'Sexo {sexo} registrado com sucesso')