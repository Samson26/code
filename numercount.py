a=input()
l=len(a)
print (l)
count=0
for i in range(0,l):
    if a[i].isnumeric():
        count+=1
print (count)
