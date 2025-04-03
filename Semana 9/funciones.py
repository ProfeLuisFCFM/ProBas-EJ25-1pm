'''
#### Función Global

#def generadorDePromediosPorMateriaPorGrupo():

palabra = "Generador de promedios por materia por grupo" 
palabra = palabra.title().replace(" ","")
palabra = palabra[:1].lower() + palabra[1:]


print(palabra)
#"anitaLavaLaTina"
def nombreFuncion(args, radio=1):         
    print("operaciones",args, radio)
    return False


nombreFuncion('A')


import math 
nombreFuncion('B',math.pi)


#### Función de clase o función local

class NombreClase():
    def __init__(self):
        self.NombreVariable = "valor"
        print("hola mundo")
    
    def printNombreVariable(self):
        print(self.NombreVariable)


objetoClase = NombreClase()
objetoClase.printNombreVariable()



#### Función en linea o función Lambda 


pesoNewton = lambda masa, gravedad=9.81: masa * gravedad

print(pesoNewton(130,22.8))


'''


def sumaListaDeNumeros(*args):
    print(type(args))
    suma = sum(i for i in args)
    return suma

l2 = sumaListaDeNumeros(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

print(l2)

# Continuamos con encapsulamiento de modulos



