# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com erros
# de índices inexistentes na lista.

import os

def lista_mercado():
    lista = []
    while True:
        try:
            seleçao = input('Selecione uma opção \n[i]nserir [a]pagar [l]istar [s]air: ').lower()

            if 'i' in seleçao:
                os.system('cls')
                item = input('Item: ')
                lista.append(item)
            
            elif 'a' in seleçao:
                os.system('cls')
                if len(lista) == 0:
                    print('A lista está vazia.')
                else:
                    print('Lista Atual.')
                    for indice, nome in enumerate(lista):
                        print(f'{indice} - {nome}')
                    indice = int(input('Escolha um Índice para apagar: '))
                    if 0 <= indice < len(lista):
                        del lista[indice]
                        os.system('cls')
                        print('Nova Lista.')
                        for indice, item in enumerate(lista):
                            print(f'{indice} - {item}')
                    else:
                        print('Índice inválido. Tente novamente.')
                
            elif 'l' in seleçao:
                os.system('cls')
                if len(lista) == 0:
                    print('Sua lista está vazia.')
                else:
                    for indice, item in enumerate(lista):
                        print(f'{indice} - {item}')

            elif 's' in seleçao:
                os.system('cls')
                print('Sua lista vai ficar assim.')
                for indice, item in enumerate(lista):
                    print(f'{indice} - {item}')
                break
            
                
            else:
                print('Opção Inválida. Tente Novamente.')


        except:
            print('Opção inválida. Tente novamente.')

lista_mercado()