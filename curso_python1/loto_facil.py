import random

def gerar_numeros_loto_facil():
    numeros = list()
    while len(numeros) < 5:
        try:
            n = int(input("Digite um número: "))
            if n > 25:
                print('Não ultrapasse do número 25.')
            elif n not in numeros:
                numeros.append(n)
            else:
                print("Valor duplicado")
        except:
            print('Digite somente números Cris.')



    numeros_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]# Números pares de 2 a 14
    numeros_pares_sorteio = random.sample(numeros_pares, 7)  # Sorteia 7 números pares

    numeros_fibonacci = [1, 2, 3, 5, 8, 13]  # Números da sequência de Fibonacci
    numeros_fibonacci_sorteio = random.sample(numeros_fibonacci, 3)  # Sorteia 1 número da sequência

    numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]  # Números primos de 1 a 15
    numeros_primos_sorteio = random.sample(numeros_primos, 5)  # Sorteia 2 números primos

    numeros_bordas = [1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25]
    numeros_bordas_sorteio = random.sample(numeros_bordas, 10)  # Sorteia 3 números primos

    numeros_sorteio = (
        numeros +
        numeros_pares_sorteio +
        numeros_fibonacci_sorteio +
        numeros_primos_sorteio +
        numeros_bordas_sorteio
    )

    l = []
    for i in numeros_sorteio:
        if i not in l:
            l.append(i)

    l = random.sample(l,15) + numeros

    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)


    amostra = l1
    amostra.sort()

    return amostra

print(gerar_numeros_loto_facil())