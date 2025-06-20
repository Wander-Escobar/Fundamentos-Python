print('Analisador de empréstimos\n')

valor_casa = float(input('Informe o valor do imóvel desejado: '))
salario = float(input('Informe o seu salário: '))
parcelamento = int(input('Informe em quantos anos deseja pagar: '))

if valor_casa / parcelamento > salario * 30 / 100:
    print('Emprestimo NEGADO! \nO valor da parcela excedeu os 30% de sua renda.')
else:
    ### Sem calculo de juros.
    print(f'Empréstimo aprovado! \nSeu financiamento no valor de {valor_casa:.2f} em {parcelamento*12} meses sairá por R${valor_casa / (parcelamento*12)} reais mensais.')