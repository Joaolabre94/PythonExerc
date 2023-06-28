# quero somar os numeros pares
lista = [3,5,8,4,3,2,22,15]
def par(x):
    if x%2==0:
        return True
    else:
        return False

def valortotal(num):
    total = 0
    for cadaum in num:
        if par(cadaum):
            total = total + cadaum
    return total


print(valortotal(lista))


# valor = int(input('Digite seu valor aqui: '))
# print(f'Seu valor desejado é : {par(valor)}')
             
