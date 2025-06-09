print('Conversor de medidas (metros):')
print()
medida = int(input('Digite uma distância em metros: '))
print()

mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {}m corresponde a:'.format(medida))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))