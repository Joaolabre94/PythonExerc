lista = [0, 2, 5, 0, 8 ,9]
def regressiva(x):
    total = 0
    for cadaum in x:
        total = cadaum + total
    return total
print(regressiva(lista))