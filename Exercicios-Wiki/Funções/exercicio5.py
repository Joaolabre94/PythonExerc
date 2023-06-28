# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaimposto, custo):
    custo = custo * (taxaimposto / 100)
    return custo

def resultado():
    while True:
        try:
            imposto = float(input('Digite a taxa de imposto: '))
            custo = float(input('Digite o custo para incluir o imposto sobre as vendas: '))
            resultado = somaImposto(imposto, custo)    
            print(f'O resultado é: {resultado} ')
            break
        except:
            print('Digite valores corretos.')

resultado()


