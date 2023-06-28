# quero o valor do par mais alto
lista = [1,2,5,7,9,20,13,12,42,68]
def par(x):
    if x%2 == 0:
        return True
    else:
        return False
    
def maiornumero(num):
    maior = 0
    for cadaum in num:
        if cadaum > maior:
            maior = cadaum
    return maior

print(maiornumero(lista))
        
