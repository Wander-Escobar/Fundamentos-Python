print('Comparando números, qual é maior ?\n')

num = []

for i in range(1,6):
    valor = int(input(f'Digite o {i}º número: '))
    num.append(valor)

print(f'\nOs números digitados foram: {num}')

print(f'\nO menor número digitado é {min(num)}')
print(f'O maior número digitado é {max(num)}\n')

print(f'Os numeros digitados em ordem crescente foram: \n{sorted(num)}\n')
print(f'Os números digitados em ordem decrescente são: \n{sorted(num, reverse=True)}')