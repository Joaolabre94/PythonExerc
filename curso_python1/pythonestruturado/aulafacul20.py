#implementar uma solução em python que retorne a soma de todos os elementos pares de uma lista.
minhalista = [2,5,6,9,22,34,35,37,39]
def par(num):
    resultado =  num%2==0
    return resultado
def coco(mylist):
    total = mylist [0]
    for cadaum in mylist:
        if par(cadaum):
            total = total + cadaum
    return total
print(coco(minhalista))
