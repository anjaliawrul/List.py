a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
m=[]
while i<len(a):
    j=0
    k=[]
    while j<len(a[i]):
        b=a[i][j]
        k.append(b)
        j+=1
    m.append(k)
    i+=1
print(m)