print('Analisador completo\n')

mulher20 = 0
idade_grupo = 0
media_grupo = idade_grupo/4
idade_homem = 0
nome_homem = ''

for cont in range(1,5):
    print(f' ===== {cont}ª PESSOA =====')
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    idade_grupo += idade
    sexo = str(input('Sexo [M/F]: ')).upper()
    
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if sexo == 'M' and idade > idade_homem:
        idade_homem = idade
        nome_homem = nome

print(f'\nA média de idade do grupo é {idade_grupo/4:.1f} anos')
print(f'O homem mais velho tem {idade_homem} anos e se chama {nome_homem}.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos')