def rec(n):
     if n < 2:
          return (n - 1)


print(rec(1))

x = 10
def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)

print(regressiva(x))