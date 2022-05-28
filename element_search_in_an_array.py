n=int(input())
f=0
a=list(map(int,input().split()))
m=int(input())
for i in a:
    if(i==m):
       f=1
       break
    else:
        f=0
if(f==1):
     print(True)
else:
     print(False)
        