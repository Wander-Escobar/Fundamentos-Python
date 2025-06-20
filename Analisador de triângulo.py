print('Analisador de triângulos\n')

seg1 = float(input('Informe o primeiro segmento: '))
seg2 = float(input('Informe o segundo segmento: '))
seg3 = float(input('Informe o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\nOs segmentos apresentados PODEM FORMAR um triângulo.')
else:
    print('\nOs segmentos apresentados NÃO PODEM FORMAR um triângulo.')