print('Detector de palíndromos\n')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1,-1,-1):
    #print(junto[letra], end='')
    inverso += junto[letra]

if junto == inverso:
    print('\nA frase informada é um palíndromo.')
else:
    print('\nA frase informada não é um palíndromo.')

