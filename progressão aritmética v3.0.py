print('Gerador de PA')
print('=' * 20)

primeiro_termo = int(input('\nPrimeiro termo: '))
razao_pa = int(input('Razão da PA: '))

c = 10
total = 10

print(f'{primeiro_termo} -> ', end='')
while True:
    while c >= 1:
        print(f'{primeiro_termo+razao_pa} -> ',end='')
        primeiro_termo += razao_pa
        c -= 1
    print('PAUSA\n')
    mais_termos = int(input(f'\nQuantos termos deseja mostrar a mais? '))
    c =+ mais_termos
    total += mais_termos
    if mais_termos == 0:
        print(f'Progressão finalizada com {total} termos apresentados.')
        break
        
    