
print('Calculadora de tinta')
print()

while True:
    
    larg = input('Largura da parede: ')
    alt = input('Altura da parede: ')    

    try:
        larg = float(larg)
        alt = float(alt)
        break
    except ValueError:
        print('Opção inválida, informe os parâmetros novamente.')
        print()
        continue         

area = larg * alt
litros = area / 2

print()
print('Sua parede tema a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².]'.format(larg, alt,area))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(litros))