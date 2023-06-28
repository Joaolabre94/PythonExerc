#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#   n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e 
#imprima até a n-ésima linha.
def imprimir_padrao():
    n = int(input("Digite um número inteiro: "))
    for i in range(1, n + 1):
        linha = ""
        for j in range(i):
            linha += str(i) + " "
        print(linha)


# Exemplo de uso da função
imprimir_padrao()



