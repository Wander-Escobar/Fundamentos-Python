print('Primeira e última ocorrencia de ultima string')
print()

frase = str(input('Digite uma frase: ')).strip().lower()

print()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra "A" aparece na posição {}.'.format(frase.find('a')+1))
print('A última letra "A" aparece na posição {}.'.format(frase.rfind('a')+1))