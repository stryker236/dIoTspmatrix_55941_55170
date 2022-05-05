import os
from Position import*
from MatrixSparseDOK import*
os.system("cls")

print("------------------Start------------------------")
m1 = MatrixSparseDOK()
m1_data = {(6, 2): 6.2, (6, 3): 6.3, (7, 4): 7.4, (8, 1): 8.1, (8, 2): 8.2, (8, 5): 8.5}
res = ((6, 1), 0.0, (8.1, 8.2, 6.2, 6.3, 8.5, 7.4, 0.0), (8, 8, 6, 6, 8, 7, -1), (1, 2, 0))
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
print("M1: ")
print(m1)
print()
teste = m1.compress()
print("Compressed")
print(teste)
print()
print("Aqui: ",teste)
print("Aqui: ",res)
print(len(teste))
print(len(res))
print(teste == res)

for x in teste:
    print(type(x))
print()
for x in res:
    print(type(x))

# a = (("ola","adeus"),("adeus","bye"))
# b = (("ola","adeus"),("adeus","bye"))
# print(a == b)
