#Elegante

path = "C:\\Users\\AULA 120\\Documents\\Github\\ProBas-EJ25\\Semana 10\\"

nombre = "divideyvenceras.py"

nombre2 = "recursivo.py"

file = open(path+nombre,"r")

for line in file:
    print(line)

file.close()


#No Elegante

with open(path+nombre2,"r",encoding="utf8") as fichero2:
    for linea in fichero2.readlines():
        print(linea)