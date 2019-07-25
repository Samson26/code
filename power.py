a=int(input())
count=0
for i in range(0,50):
  if(pow(2,i)==a):
    print("yes")
    count+=1
if(count==0):
  print("no")
