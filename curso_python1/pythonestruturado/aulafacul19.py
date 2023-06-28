minhaLista = [2,5,6,7,10,11,31,46,2]
def par(num):
    if num%2==0 :
        return True
    else:
        return False

def somaPares(myList):
    total = 0
    for valor in myList:
        if par(valor):
            total = total + valor
    return total

print(somaPares(minhaLista))
