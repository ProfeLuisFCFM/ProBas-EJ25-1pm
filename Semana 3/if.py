num1 = 5
num2 = 3

condicion = num1 > num2

cond = bool(0.00)
print(condicion,cond)
if condicion:
    print("si")
    
    
if cond:
    print("Accion")
    

if cond:
    print("verdadero")
else:
    print("falseo")
    
cond1 = True
while cond1:
    edad = int(input("captura edad"))
        
    if edad < 18:
        print("eres menor")

    elif edad>=18 and edad <= 60:
        print("eres adulto")
        
    elif edad >= 60 and edad <= 99:
        print("Saca beca Bienestar")
        
    else:
        print("ya no puedes usar LEGOs")
    
    if edad == 120:
        cond1 = False

    