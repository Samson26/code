a=input()
l=len(a)
c=a[l-1]
b=[]
str=""
for i in range(0,l-2):
    b.append(a[i])
for i in range(0,int(c)):
    print(str.join(b))
