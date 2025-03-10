'''
#Tipos básicos
int()
float()
#Tipo básico pero aspira a compuesto
str()
#Tipos compuestos
list()
set()
tuple()
#Tipo compuesto que combina otros tipos compuestos
dict()
'''

mensaje = "Johanne Sacreblue"
'''
print(mensaje.capitalize())

print(mensaje.count("a"))

mensaje += "𐤃 · Δδ"

with open("rarito.txt","w",encoding='utf8') as file:
    print(mensaje, file=file)

with open("rarito.txt", "r" ,encoding='utf8') as fichero:
    print(fichero.readlines())
'''


#tabs = "A\tB\tC\tD\tE\tF\tE"
#tabs.expandtabs(2)
#print(tabs)

#print(mensaje.index('a'))

#indicesE = []

#for indice in range(len(mensaje)):
#    if mensaje[indice] == 'e':
#        indicesE.append(indice)
#    #print(mensaje[indice], end=" ")
#print(indicesE)

idx = 0
id = -1
lista=[]
tamanio = len(mensaje)
while idx != tamanio:
    if mensaje.index('e') != None:
        id = mensaje.index('e')
        print(id)
        mensaje = mensaje[id:]
        lista.append(id+idx)
        idx+=id
    else:
        break
    
print(lista) 


