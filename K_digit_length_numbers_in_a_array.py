a,b=map(int,input().split())
c=list(map(int,input().split()))
#print(a,b,c)
d=0
for i in c:
    if(i<0):
        i=i*(-1)
    k=len(str(i))
    if(k==a or k==b):
        d=d+1
    else:
         k=len(str(i))
         if(k==a or k==b):
             d=d+1
print(d)