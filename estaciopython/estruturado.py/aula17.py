#FIBONACCI
#A sequência de Fibonacci é: 1, 1, 2, 3, 5, 8, 13, 21... Os dois primeiros termos são 1; a partir do 3º termo, 
#cada termo é a soma dos dois anteriores.

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(help(fibo))