import random

def generar_edades():
    lista = []
    for i in range(1, 11):
        lista.append(dict(id = i, edad = random.randint(1,100)))  
    return lista
