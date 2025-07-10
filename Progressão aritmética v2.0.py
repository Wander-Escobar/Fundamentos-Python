print('Gerador de PA')
print('='*15)

primeiro_termo = int(input('\nPrimeiro termo: '))
razao_pa = int(input('Razão da PA: '))

c = 10

while c > 0: 
    if c == 10:
        print(f'{primeiro_termo} -> ', end = '')
        c -= 1
    else:
        print(f'{primeiro_termo+razao_pa} -> ', end = '')
        primeiro_termo += razao_pa
        c -= 1

print('FIM')
