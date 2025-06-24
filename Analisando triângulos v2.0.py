print('Analisando triângulos v2.0\n')

s1 = int(input('Digite o primeiro segmento: '))
s2 = int(input('Digite o segundo segmento: '))
s3 = int(input('Digite o terceiro segmento: '))

if s1 == s2 and s1 == s3 and s3 == s1:
    print('\nOs segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif s1 == s2 or s2 == s3 or s3 == s1:
    print('\nOs segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('\nOs segmentos acima PODEM FORMAR um triângulo ESCALENO!')