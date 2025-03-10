"""def presentar(nombre, edad, ciudad):
    print(f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}.")

presentar("Carlos", 25, "Monterrey")
presentar(25, "Carlos", "Monterrey") # Error lógico
presentar(nombre="Carlos", ciudad="Monterrey", edad=25)
presentar("Carlos", edad=25, ciudad="Monterrey")
presentar(edad=25, "Carlos", ciudad="Monterrey") # Error de sintaxis

"""
"""
def calcular_precio(precio, impuesto=0.16, descuento=0):
    precio_final = precio + (precio * impuesto) - descuento
    return precio_final # Pruebas
print(calcular_precio(100)) # Usa impuesto por defecto y sin descuento
print(calcular_precio(100, 0.20)) # Cambia el impuesto, pero sin descuento
print(calcular_precio(100, descuento=10)) # Aplica descuento pero usa el impuesto por defecto
print(calcular_precio(100, descuento=5, impuesto=0.18)) # Cambia ambos

"""

pares = [1,2,3]
if "1" in pares:
    print("Sí, 1 esta en la lista")
else:
    print("No esta")