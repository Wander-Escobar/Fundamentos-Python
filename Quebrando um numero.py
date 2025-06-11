print('Quebrando um numero e mostrando apenas a porção inteira.')
print()

import math

num = float(input('Digite um número: '))
print()

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num,math.trunc(num)))