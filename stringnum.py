a=input()
b=a
b=str(b)
l=len(b)
c=0
count=0
for i in range(0,l):
    try:
        c=int(b[i])+1
        count+=1
    except:
        continue
if(count>0):
    print("Yes")
else:
    print("No")
    
