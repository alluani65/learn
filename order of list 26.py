l=['a','a','b','c']
a=set()
L=[i for i in l if not (i in a or a.add(i))]
print(L)