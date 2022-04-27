import os
os.system("cls")

'''Aqui está muito resumidamente o algoritmo das iterações e dos next'''
d = {
    (2,1):1,
    (4,4):2,
    (1,1):3
}

d += 1
print(d)

# aux = iter(d)
# print(aux)
# print(type(aux))
# print(len(d))

# print(next(aux))
# print(next(aux))
# print(next(aux))


aux = sorted(d)
print(d)
print(aux)
print(type(aux))