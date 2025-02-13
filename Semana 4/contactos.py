

bandera = True
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
    
    

print(ListaContactos)

