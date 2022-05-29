n=int(input())
a=list(map(int,input().split()))
sum=0
f=0
k=len(a)
#print(a)
for i in a:
   if(i==0 or i==1):
       f=f+1
if(f==k):
    print(True)
else:
    print(False)
       