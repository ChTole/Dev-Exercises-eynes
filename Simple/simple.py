import random

def generar_edades():
    lista = []
    for i in range(1, 11):
        lista.append(dict(id = i, edad = random.randint(1,100)))  
    return lista

def ordenar_edades(lista):
    def capturar_edad(edad):
        return edad['edad']
    lista.sort(reverse=True, key=capturar_edad)
    print("id persona más joven: ", lista[-1]["id"])
    print("id persona más anciana: ", lista[0]["id"])
    return lista

edades = ordenar_edades(generar_edades())