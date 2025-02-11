#Busqueda lineal:

from random import randint

listaP = list()
listaN = list()
elementos = int(input("Introduce la cantidad de elementos: "))

for cont in range(-elementos, elementos):
    if cont < 0:
        listaN.append(randint(-100,0))
    elif cont > 0:
        listaP.append(randint(1,100))
    else:
        listaP.append(randint(0,1))
        
listaCompleta = listaN + listaP

print(listaCompleta)

listaN.extend(listaP)

print(listaN)


num = int(input("Introduce un número a buscar: "))

for itm in listaCompleta:
    if itm == num:
        print("El numero se encontraba en la posición ", listaCompleta.index(itm))
        break


## Busqueda binaria:

# Leer sobre el algoritmo de Divide y Vencerás!



        
    
    
    
    


