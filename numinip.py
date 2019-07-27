a=input()
l=len(a)
for i in range(0,l):
    if(type(a[0][i])=="int"):
        print("Yes")
        break
    else:
        print("No")
