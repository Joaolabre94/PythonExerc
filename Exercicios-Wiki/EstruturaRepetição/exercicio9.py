# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
def impar(y):
    if y % 2 == 0:
        return False
    else:
        return True

for x in range(0, 51):
    if impar(x):
        print(x)