import random

matriz = []
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(random.randint(1, 5))

for k in matriz:
    print(k)