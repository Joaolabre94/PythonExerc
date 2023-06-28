#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def letra():
    letra_digitada = input('Digite uma letra: ')
    if letra_digitada in 'AEIOUaeiou':
        return 'Vogal'
    else:
        return 'Consoante'
print(f'Sua letra digita é: {letra()}')