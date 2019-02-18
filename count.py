a=map(str,raw_input().split())
n=len(a)
c=0
i=0
while i<n:
    b=len(a[i])
    c+=b
    i+=1
print c
