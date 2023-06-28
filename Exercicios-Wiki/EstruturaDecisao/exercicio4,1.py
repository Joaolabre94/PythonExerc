#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
if letra in 'AEIOUaeiou' :
    print(f'É uma vogal: {letra}')
else:
    print(f'É uma consoante: {letra}')