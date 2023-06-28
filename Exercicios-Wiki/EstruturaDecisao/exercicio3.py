#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
    sexo = input('Digite o sexo (F/M): ')
    if sexo == 'F' : 
        print('Feminino')
        break
    elif sexo == 'M':
        print('Masculino')
        break
print('Digite o valor correto')