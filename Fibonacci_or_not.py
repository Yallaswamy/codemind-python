n=int(input())
a=0
k=0
b=1

#print(a,b)
for i in range(1,n):
    f=a+b
  #  print(i)
    if(f==n):
        k=1
    a=b
    b=f
   
if(k==1):
    print(True)
else:
    print(False)
