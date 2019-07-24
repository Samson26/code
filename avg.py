a=int(input())
arr=[int(i) for i in input().split()]
b=0
for i in range(0,a):
	b+=arr[i]
c=b//a
print(c)
