while True:
    print('Conversor de moedas')
    dinheiro = (input('Quanto dinheiro você deseja converter? R$'))
    print()

    try:
        dinheiro = float(dinheiro)
        break
    except ValueError:
        print('Opção inválida! Digite um número válido.')
        continue

result = dinheiro / 3.27
print('Considerando o dolar a US$ 3,27:')
print('Com R${:.2f} reais você pode comprar US${:.2f} dolares americanos'.format(dinheiro,result))