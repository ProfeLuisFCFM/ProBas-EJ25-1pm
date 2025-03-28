def suma(n):
    suma = 0
    for i in range(1,n+1):
        suma += i
    return suma

def suma2(n):
    suma = 0
    for i in range(1,(n//2)+1):
        suma += i 
        suma += (n+1-i) 
    return suma

def suma4(n):
    suma = 0
    for i in range(1,(n//4)+1):
        suma += i 
        suma += (n+1-i) 
        suma += (n//2)+i 
        suma += (n//2)+(1-i) 
    return suma
 

import time

def cuantoDura(funcion):
    inicio = time.time()
    funcion(1000000000)
    return (time.time() - inicio)


print(cuantoDura(suma))
print(cuantoDura(suma2))
print(cuantoDura(suma4))



