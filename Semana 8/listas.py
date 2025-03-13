#numeros = [10, 20, 30, 40]
#for num in numeros:
#    print(num)


#numeros = [10, 20, 30, 40]
#for i in range(len(numeros)):
#    print(f"Indice {i}: {numeros[i]}")
   
#frutas = ["Manzana", "Banana", "Naranja"]
#for i, x in enumerate(frutas):   
#    print(f"{i}: {x}")

nombres = ["Carlos", "Ana", "Luis"]
notas = [90, 85, 88]
for nombre, nota in zip(nombres, notas):   	
    print(f"{nombre} obtuvo {nota}")


for i in enumerate(nombres):
    print(i)
    

"""
def multiplicar_por_dos(numero):
    return numero * 2
numeros = [1, 2, 3, 4, 5]
resultado = list(map(multiplicar_por_dos, numeros))
print(resultado)

numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros))
print(resultado)

numeros = [5, 12, 7, 20, 30, 3]
def es_mayor_que_10(numero):
    return numero > 10
resultado = list(filter(es_mayor_que_10, numeros))

numeros = [5, 12, 7, 20, 30, 3]
resultado = list(filter(lambda x: x > 10, numeros))
print(resultado)
"""