# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com erros
# de índices inexistentes na lista.

import os

lista = []
def inserir(i):
    if 'i' == i:
        os.system('cls')
        item = input('Item: ')
        lista.append(item)

def apagar(a):
    if 'a' == a:
        os.system('cls')
        if len(lista) == 0: 
            print('A lista está vazia.')
        else:
            print('Lista Atual.')
            for indice, nome in enumerate(lista):
                print(f'{indice} - {nome}')
            indice = int(input(f'Escolha um índice para apagar: '))
            if 0 <= indice < len(lista):
                del lista[indice] 
                os.system('cls')
                print('Nova Lista.')
                for indice, nome in enumerate(lista):
                    print(f'{indice} - {nome}')
            else:
                print('Índice inválido. Tente novamente.')

def listar(l):
    if 'l' == l:
        os.system('cls')
        if len(lista) == 0:
            print('A lista está vazia.')
        else:
            print(f'Lista de compras')
            for indice, nome in enumerate(lista):
                print(f'{indice} - {nome}')

def sair(s):
    if 's' == s:
        os.system('cls')
        print('Você saiu do programa, sua lista ficou assim.')
        for indice, nome in enumerate(lista):
            print(f'{indice} - {nome}')
            


def lista_mercado():
    while True:
        try:
            seleçao = input('Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()

            inserir1 = inserir(seleçao)

            apagar1 = apagar(seleçao)

            listar1 = listar(seleçao)

            if 's' == seleçao:
                sair1 = sair(seleçao)
                break
        except:
            print('Opção Inválida. Tente Novamente.')
            
lista_mercado()
