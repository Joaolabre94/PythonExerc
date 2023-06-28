#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Escreva a letra desejada: ')
if letra in 'AEIOUaeiou':
    print('vogal')
else:
    print('Consoante')