d1 = dict()
d1[1] = 'uno'
d1[2] = "dos"
d1[3] = '''Tres'''
d1[6] = """Seis"""

d2 = {}
d2['a'] = "a"
d2['b'] = "be"
d2['c'] = "ce"
d2['d'] = "de"



print(d1,type(d1),'\n',d2,type(d2))

#d1.clear()

#print(d1)

d3 = d1.copy()

d3[1484412] = 'matricula del profe'
print(d1,d3)


print(d1.fromkeys({1,7}))

print(d1.get(2))

print(d1.items())

for k,v in d1.items():
    print(k,v)

print(d1.keys())

#d3.pop(1484412)

#print(d3)

#d3.popitem()

#print(d3)

d1.setdefault(7)

d1[8] = None

print(d1)

d1.update({17:'diecisiete', 18: "dieciocho", 19: 'diecinueve', 20: 'veinte', 21: 'veintiuno'})

print(d1)
d1[1] = 'once'
print(d1)
print(d1.values())


