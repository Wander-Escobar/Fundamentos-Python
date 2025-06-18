print('Calculadora de aumento de salário\n')

salario = float(input('Informe o salário a ser reajustado: '))

### Salários acima de R$1250.00 recebem aumento de 10%
### Salários acima de R$1250.00 recebem aumento de 15%
### reajuste_15 = salario*15/100)+salario
### reajuste_10 = salario*10/100)+salario

if salario <= 1250.00:
    print(f'\nO salário de R${salario} passará para R${(salario*15/100)+salario}') ### Valor da 2º chave pode ser substituida por reajuste_15
else:
    print(f'\nO salário de R${salario} passará para R${(salario*10/100)+salario}') ### Valor da 2º chave pode ser substituida por reajuste_10

