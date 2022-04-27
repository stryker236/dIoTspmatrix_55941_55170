import os
os.system("cls")

'''Aqui está muito resumidamente o algoritmo das iterações e dos next'''
d = {
    (2,1):1,
    (4,4):2,
    (1,1):3
}

aux = {("ola",1):1}
for k,v in aux.items():
    print(type(k))
    print(type(v))

# aux = (1,1,1)
# a,b,c,d = aux
# print(a,b,c)

# aux = iter(d)
# print(aux)
# print(type(aux))
# print(len(d))

# print(next(aux))
# print(next(aux))
# print(next(aux))

'''Testagem do sorted'''
# aux = sorted(d)
# print(d)
# print(aux)
# print(type(aux))