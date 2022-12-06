import random

matriz = []
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(random.randint(1, 5))

for k in matriz:
    print(k)
    
for i in range(len(matriz)):
    for j in range(len(matriz[i]) - 3):
        if matriz[i][j] == matriz[i][j + 1] - 1 == matriz[i][j + 2] - 2 == matriz[i][j + 3] - 3:
            inicia = f"fila {i + 1} - columna {j + 1}"
            final = f"fila {i + 1} - columna {j+3 + 1}"