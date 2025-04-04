#Elegante

path = {
        'FCFM': "C:\\Users\\AULA 120\\Documents\\Github\\ProBas-EJ25\\Semana 10\\",
        'Personal': "C:\\Users\\luisG\\OneDrive\\Documentos\\GithubFCFM\\ProBas-EJ25-1pm\\Semana 10\\"  
        }


nombre = "divideyvenceras.py"

nombre2 = "recursivo.py"

file = open(path['Personal']+nombre,"r")

for line in file:
    print(line)

file.close()


#No Elegante

with open(path['Personal']+nombre2,"r",encoding="utf8") as fichero2:
    for linea in fichero2.readlines():
        print(linea)

edad = 18

with open("escritura.txt", "w", encoding="utf8") as fich:
    fich.write("hola\tmundo\tdesde monterrey a 45°C\n")

    print(f"La mayoría de edad es a los {edad} años.", file=fich)