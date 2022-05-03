m2 = m1 + 1
m2_data = {(1, 1): 2.1, (1, 2): 2.2, (1, 3): 2.3, (2, 1): 3.1, (2, 2): 3.2, (2, 3): 3.3}
print("m2:")
print(m2)
print()
print("m1:")
print(m1)
print()
for key, value in m2_data.items():
    print("Teste1: ",value, m2[Position(key[0], key[1])])
print("Teste2: ",m2.zero, m1.zero)
print("Teste3: ",len(m2_data), len(m2))
for key, value in m1_data.items():
    print("Teste4: ",value, m1[Position(key[0], key[1])])