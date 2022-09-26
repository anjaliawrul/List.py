a=[[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
i=0
b=[]
while i<len(a):
    c=[a[i],a[i+1],a[i+2]]
    b.append(c)
    i=i+4
print(b)



# a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# size=int(input("enter the size:"))
# i=0
# b=[]
# while i<len(a):
#     x=a[i:i+size]
#     b.append(list(x))
#     i=i+size
# print(b)       