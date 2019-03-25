a=int(input())
b=1
c=1
print('1'+" "+'1',end=" ")
for i in range(0,a-2):
    d=b+c
    print(d,end=" ")
    b=c
    c=d
