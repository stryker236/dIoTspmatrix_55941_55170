import os
from Position import*
from MatrixSparseDOK import*
os.system("cls")

print("------------------Start------------------------")

m1 = MatrixSparseDOK()
m1_data = {(1, 1): 1, (1, 3): 2, (2, 1): 3, (2, 3): 4}
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
m2 = MatrixSparseDOK()
m2_data = {(1, 1): 1, (1, 2): 2, (3, 1): 3, (3, 2): 4}
for key, value in m2_data.items():
    m2[Position(key[0], key[1])] = value

m3 = m1 * m2

print("M1: ")
print(m1)
print()

print("M2: ")
print(m2)
print()

print("M3: ")
print(m3)
print()
m3_data = {(1, 1): 7, (1, 2): 10, (2, 1): 15, (2, 2): 22}
for key, value in m3_data.items():
    print(value, m3[Position(key[0], key[1])])