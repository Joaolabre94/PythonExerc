# soma de toda a lista

lista = [1,4,5,6,7,10,20,4,3]


# def foo(n):
#     total = 0
#     for cadaum in (n):
#         total = total + cadaum
#     return total


# print(foo(lista))
    

def par(n):
    if n%2==0:
        return True
    else:
        return False
    
def valores(n):
    total = 0
    for num in n:
        if par(num):
            if num > total:
                total = num
    return total
        
print(valores(lista))