#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def verificar_sexo():
    while True:
        resultado = input('Escreva seu sexo [F/M]: ').lower()
        if resultado == 'f':
            return 'Feminino!'
        elif resultado == 'm':
            return 'Masculino!'
        else:
            return 'Escreva o valor correto!'
    
    
print(f'Seu sexo é: {verificar_sexo()}')
