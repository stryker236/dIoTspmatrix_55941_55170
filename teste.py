import os
from Position import*
from MatrixSparseDOK import*
os.system("cls")

m = MatrixSparseDOK()
m2 = m.__copy__()
m2.zero = 1e7
m[1, 1] = 1.1
print(1e7, m2[1, 1])
print(0, len(m2))
print(1, len(m))