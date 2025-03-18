conjunto = {1,2,3,4}

conjunto2 = {3,4,5,6}


print(type(conjunto),type(conjunto2))

#conjunto.add('A')
#conjunto.add('a')

#print(conjunto)

#conjunto.clear()
#print(conjunto)

conjunto3 = conjunto.copy()

#print(conjunto3)

print(conjunto.difference(conjunto2))

conjunto.discard(7)

print(conjunto.intersection(conjunto2))

print(conjunto.isdisjoint(conjunto2))


subset = {1,4}

print(subset.issubset(conjunto))

superset = {1,2,3,4,5,6,7,8,9,10}

print(superset.issuperset(conjunto))

print(conjunto.issubset(superset))

#conjunto.pop()
#print(conjunto)

#conjunto.add(5)
#print(conjunto)
#conjunto.remove(5)
#print(conjunto)


print(conjunto.symmetric_difference(conjunto2))

print(conjunto.union(conjunto2))
print(conjunto)

conjunto.update(conjunto2)

print(conjunto)

#conjunto.difference_update() #1,2
#conjunto.intersection_update() #3,4
#conjunto.symmetric_difference_update() #1,2,5,6