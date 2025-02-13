

bandera = False
contador = 1
ListaContactos = list()

while bandera:    
    op = input(f"Cantidad de contactos: {contador-1} \n Desea agregar un contacto?(S/N): ")
    if op.lower() == 's':
        contacto = dict()
        contacto["identificador"] = input(f"Ingrese el identificador de contacto {contador}: ")
        contacto["número"] = input(f"Ingrese el número de contacto {contador}: ")
        contador += 1
        ListaContactos.append(contacto)
    else:
        break
    
    

#print(ListaContactos)


#from random import randint

#import pandas as pd

#import matplotlib.pyplot as plt


## Problema 17

#Pila, Cola, lista enlazada

pila = list()

def insertarPila(pila, elemento):
    pila.append(elemento)
    return pila

def eliminarPila(pila):
    elementoFinal = pila[len(pila)-1]
    pila.remove(elementoFinal)
    return pila


if __name__ == "__main__":
    estupila = list()
    insertarPila(estupila,1)
    print(estupila)
    insertarPila(estupila,"mi pelo")
    print(estupila)
    insertarPila(estupila,"ideota")
    print(estupila)
    eliminarPila(estupila)
    print(estupila)

