#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
while True:
    sexo = input('Informe seu sexo [F/M]: ').upper()
    if sexo == 'M':
        print('Seu sexo é masculino')
        break
    elif sexo == 'F':
        print('Seu sexo é feminino')
        break
    else:
        print('Sexo Inválido')
    