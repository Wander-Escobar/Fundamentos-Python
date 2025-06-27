print('='*21)
print('10 termos de uma PA')
print('='*21,'\n\n')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print()

for cont in range(termo,10*razao+termo,razao):
    print(cont, end=' -> ')

print('ACABOU!')