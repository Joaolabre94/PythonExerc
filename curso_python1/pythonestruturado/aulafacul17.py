# Implementar uma solução em que calculer o fatorial de um número n! ex, 5! =5.4.3.2.1= 120
#fatorial de numero n! = n(n-1)
def fatorial_interativo(n):
    f=1
    for i in range(1, n+1):
        f = f*i
        return f
    

