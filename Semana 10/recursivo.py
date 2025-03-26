def fibbo(num):
    lst = list()
    if num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        lst = [0,1]        
        for it in range(2,num+1):
            lst.append(lst[it-2]+lst[it-1])
    return lst

#print(fibbo(1000))

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
            
def fiboR(n,fib_list=[0, 1]):
    # Si n ya está calculado, devolver el valor almacenado
    if n < len(fib_list):
        return fib_list[n]
    
    # Si no, calcularlo de manera recursiva y almacenar el valor
    fib_list.append(fiboR(n-1, fib_list) + fiboR(n-2, fib_list))
    with open("fibo_mem.txt","w") as fibomem:
        print(fib_list, file=fibomem)
    return fib_list[n]

    
# Ejemplo de uso:
n = 10  # Número de Fibonacci que deseas calcular
print(f"F({n}) = {fiboR(n)}")

with open("fibo_mem.txt","r") as fil:
    v = fil.readline()
    print(v)

        