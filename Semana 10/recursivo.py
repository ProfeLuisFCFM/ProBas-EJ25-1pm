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

print(fibbo(1000))
            
def fibboRecursivo():
    pass
    