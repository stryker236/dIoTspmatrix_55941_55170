import os
from Position import*
from MatrixSparseDOK import*
os.system("cls")

m1 = MatrixSparseDOK()
m1_data = {(2, 3): 2.3, (1, 3): 1.3, (2, 2): 2.2, (1, 2): 1.2, (2, 1): 2.1, (1, 1): 1.1}
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
test = {(1, 1): 1.1, (1, 2): 1.2, (1, 3): 1.3, (2, 1): 2.1, (2, 2): 2.2, (2, 3): 2.3}
test_list = list(test)
i = 0
for pos in m1:
    print(m1_data[test_list[i]], m1[pos])
    i += 1