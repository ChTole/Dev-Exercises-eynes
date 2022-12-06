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
            inicia_h = f"fila {i + 1} - columna {j + 1}"
            final_h = f"fila {i + 1} - columna {j+3 + 1}"
            
for i in range(len(matriz) - 3):
    for j in range(len(matriz[i])):
        if matriz[i][j] == matriz[i + 1][j] - 1 == matriz[i + 2][j] - 2 == matriz[i + 3][j] - 3:
            inicia_v = f"fila {i + 1} - columna {j + 1}"
            final_v = f"fila {i+3 + 1} - columna {j + 1}"