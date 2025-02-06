"""clave = ""
while clave != "1234":
    clave = input("Ingrese la clave: ")
print("Acceso concedido.")

contador = 1
while contador <= 5:
    if contador == 3:
        print("Se interrumpe el bucle en", contador)
        break # Rompe el bucle cuando contador es 3
    print("Iteración número", contador)
    contador += 1
    
    
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue # Salta la impresión cuando contador es 3
    print("Iteración", contador)
    

contador = 0
while contador < 8:
    contador += 1
    if contador == 3:
        print("Saltando número 3 con continue")
        continue # Salta la iteración con 3
    if contador == 5:
        print("Interrumpiendo el bucle con break")
        break # Detiene el bucle cuando contador es 5
    print("Iteración", contador)
    

numero = int(input("Ingrese un número: "))
contador = 0
while contador <= numero:
    print(contador)
    contador += 2 # Incrementamos en 2 para solo imprimir pares
    
"""    
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            break # Sale del bucle si la edad es válida
        print("Por favor, ingrese un número mayor que 0.")
    except ValueError:
        print("Error: Ingrese un número válido.")
