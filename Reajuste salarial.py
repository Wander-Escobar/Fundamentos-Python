print('Calculo de reajuste salarial')
print()

salario = input('Qual é o salário do funcionário? R$')

while True:
    try:
        salario = float(salario)
        print()
        break
    except ValueError:
        print('Valor inválido, tente novamente.')
        print()
        continue


novosal = salario + (salario * 15 / 100)

print(' Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novosal))