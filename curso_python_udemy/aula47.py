"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
def valores():
    nome1 = input('Digite seu nome: ')
    idade1 = input('Digite sua idade: ')
    if len(nome1) < 1:
        print('Desculpe, você deixou campos vazios!')
        return
    elif len(idade1) < 1:
        print('Desculpe, você deixou campos vazios!')
        return
    print(f'Seu nome é: {nome1}')
    print(f'Seu nome invertido é: {nome1[::-1]}')
    if ' ' in nome1:
        print(f'Seu nome contém espaços!')
    else:
        print(f'Seu nome não possui espaços!')
    print(f'Seu nome tem: {len(nome1)} letras')
    print(f'A primeira letra do seu nome é: {nome1[0:1:]}')
    print(f'A ultima letra do seu nome: {nome1[-1::]}')



variaveis = valores()