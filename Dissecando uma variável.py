var = input('Digite algo: ')

#verifica o tipo primitivo da variável
print('O tipo primitivo da variável é: ',type(var))

#verifica se só contem espaços
print('Só contem espaços? ', var.isspace())

#verifica se a variável é um número
print('É um número? ', var.isnumeric())

#verifica se é alfabético 
print('É alfabético? ', var.isalpha())

#verifica se é alfanumérico
print('É alfanumérico? ', var.isalnum())

#verifica se está maiúscula
print('Está maiúscula? ',var.isupper())

#verifica se está minúscula
print('Está minúscula? ', var.islower())

#verifica se está capitalizada
print('Está capitalizada? ', var.istitle())