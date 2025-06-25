print('====== Lojas Escobar ======\n\n')

valor_produto = float(input('Informe o valor do produto: R$ '))

print('\nOPÇÕES DE PAGAMENTO:')
print('[ 1 ] Pagamento à vista / cheque (10% de desconto)')
print('[ 2 ] Pagamento à vista no cartão (5% de desconto)')
print('[ 3 ] Pagamento em até 2x no cartão (preço normal)')
print('[ 4 ] Pagamento em até 3x no cartão (20% de juros)')

menu = int(input('\nQual a opção de pagamento desejada ? '))

match menu:

    case 1:
        print('\nCom pagamento à vista você receberá o desconto de 10% !')
        print(f'O produto com valor de R${valor_produto:.2f} reais sairá por R${valor_produto-(valor_produto*10/100):.2f}.')
    case 2:
        print('\nCom pagamento à vista no cartão você receberá o desconto de 5% !')
        print(f'O produto com valor de R${valor_produto:.2f} reais sairá por R${valor_produto-(valor_produto*5/100):.2f}.')
    case 3:
        print(f'\nO produto no valor de R${valor_produto:.2f} reais sairá em duas parcelas de R${valor_produto/2:.2f} reais.')
    case 4:
        parcelas = int(input('\nDeseja dividir em quantas parcelas ? '))
        parcelado = (valor_produto * 20 /100 + valor_produto) / parcelas
        print(f'\nSua compra será parcelada em {parcelas}x parcelas de R${parcelado}')
    case _:
        print('Opção inválida ! ')