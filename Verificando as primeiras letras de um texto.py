print('Na cidade informada contem a paravra "Santo"? ')
print()

cidade = str(input('Informe uma cidade para verificação: ')).strip()
print()

if cidade[0:5].lower() == 'santo':
    print('A cidade informada, começa com "Santo" !')
else:
    print('A palavra "Santo" não foi localizada na cidade informada.')
