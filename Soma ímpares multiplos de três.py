print('Somador de números ímpares multiplos de três\n')

soma_total = 0
multiplos = 0

for cont in range(1,501,2):
    if cont % 3 == 0:
        multiplos += 1
        soma_total += cont

print(f'A soma de todos os {multiplos} números ímpares multiplos de três é: {soma_total}')