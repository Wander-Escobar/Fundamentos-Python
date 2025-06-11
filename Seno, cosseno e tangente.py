print('Calculadora de Seno, Cosseno e Tangente')
print()

import math

while True:
    
    ang = input('Digite um ângulo: ')
    print()

    try:
        ang = float(ang)
        break
    except ValueError:
        print('Ângulo inválido! Tente novamente.')
        continue

rad = math.radians(ang)

print('O Seno de {} é {:.2f}'.format(ang,math.sin(rad)))
print('O Cosseno de {} é {:.2f}'.format(ang,math.cos(rad)))
print('A tangente de {} é {:.2f}'.format(ang,math.tan(rad)))


