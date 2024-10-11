
a=[]
for i in range(150,1000):
    b=i
    d=str(i)
    c=sum([int(i)**len(d)for i in d])
    if b==c:
        a.append(c)
print(a)