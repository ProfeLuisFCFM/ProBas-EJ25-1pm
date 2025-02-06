#Lista = []

#print(bool(Lista))


#list
#tuple
#set
#dict

saludos = dict()

saludos['Español'] = "Hola Mundo"
saludos['English'] = "Hello World"
saludos["Fracais"] = "Bonjour Mondieu"
saludos["Nihongo"] = "Ohayo Warudo"
saludos["Portugues"] = "Saludo al macaco" 
saludos["Portugues"] = "Holau mundou"


#print(saludos.items())

#for idioma, saludo in saludos.items():
#    print(idioma,saludo)
    
    
    
estudiambre = dict()

estudiambre["nombre"] = "Luis Gutierrez"
estudiambre["Carrera"] = "DISI"
estudiambre["semestre"] = 12


grupo77 = dict()

grupo77[1484412]=estudiambre


#print(grupo77)

primos = [1,2,3,5,7,11,13,17,19,23,29,31]


setPrimos = list()




for num in range(0,32):
    if num in primos:
        print(num)
print(setPrimos)

print(range(10))


### Como resolver el problema 10


# Método 1: con la palabra reservada with

with open("prueba.txt","w") as variable1:
    print("mensaje de texto SMS 11122", file=variable1)
    

#

# Método 2: con variable

variable2 = open("prueba2.txt","w")

#Si se hace con el método 2, es necesario cerrar la variable
print("Hola mundo desde North Korea", file=variable2)

variable2.close()


#len(variable2) medir tamaño