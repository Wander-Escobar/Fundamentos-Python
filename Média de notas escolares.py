print('Calculadora de média escolar\n')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'\nREPROVADO!!\n\nSua média foi {media} e precisava de 7.00, estude mais!!')
elif media >= 5 and media < 7:
    print(f'\nRECUPERAÇÃO!!\n\nSua média foi {media}, estude para não reprovar!!')
else:
    print(f'\nAPROVADO!!\n\nSua média foi {media}, parabéns !!!')