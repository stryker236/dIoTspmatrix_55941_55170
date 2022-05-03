import os
from Position import*
from MatrixSparseDOK import*
os.system("cls")

m1 = MatrixSparseDOK(3.0)
m1_data = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
m2 = m1.transpose()
m2_data = {(1, 1): 1.1, (2, 1): 1.2, (3, 1): 1.3, (1, 2): 2.1, (2, 2): 2.2, (3, 2): 2.3}
for key, value in m2_data.items():
    print("Teste1",value, m2[Position(key[0], key[1])])
print("Teste2",m2.zero, m1.zero)
print("Teste3",len(m2_data), len(m2))
print("aux: ",m2._items)
for key, value in m1_data.items():
    print("Teste4",value, m1[Position(key[0], key[1])])
print("Teste5",len(m1_data), len(m1))