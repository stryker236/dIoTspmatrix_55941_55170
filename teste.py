import os
from re import M
from Position import*
from MatrixSparseDOK import*
os.system("cls")

m = MatrixSparseDOK()
m[Position(1, 2)] = 1.2
m[Position(2, 1)] = 2.1
print("0 1.2\n2.1 0")
print("antes")
print(str(m))
print("depois")