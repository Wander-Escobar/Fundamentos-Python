print('Procurando uma string dentro de outra')
print()

nome = str(input('Digite seu nome completo: ')).strip().lower()
print()

print('Possui Silva no nome ? {}'.format('silva' in nome))