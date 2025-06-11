print('Calculadora de catetos e hipotenusa')
print()

from math import sqrt
from math import pow

while True:

    catop = input('Digite o comprimento do cateto oposto: ')
    catad = input('Digite o comprimento do cateto adjacente: ')
    print()

    try:
        catop = float(catop)
        catad = float(catad)
        break
    except:
        print('Valor inválido! Digite novamente.')
        print()
        continue

hip = sqrt(pow(catop,2)+pow(catad,2))

print('Considerando o cateto oposto {:.1f} e o cateto adjacente {:.1f}, a hipotenusa é {:.2f}.'.format(catop,catad,hip))