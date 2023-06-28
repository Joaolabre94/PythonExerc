lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def solution3(number):
    if number % 3 == 0:
        return True
def solution5(number):
    if number % 5 == 0:
        return True
def conclusion3(x):
    lista = 0
    for eachone in x:
        if solution3(eachone):
            lista = eachone + lista
    return lista
def conclusion5(x):
    lista = 0
    for eachone in x:
        if solution5(eachone):
            lista = eachone + lista
    return lista

print(f'Soma dos divisiveis por 3: {conclusion3(lista)}')
print(f'Soma dos divisiveis por 5: {conclusion5(lista)}')