n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())

c=0
d=[]
for i in m:
    if(i in range(a,b+1)):
        d.append(i)
        c=c+1
if(c>0):
    print(min(d))
else:
    print(-1)