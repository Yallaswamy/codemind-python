n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
c=0
for i in m:
    if(i in range(a,b+1)):
        d.append(i)
        c=c+1
if(c>0):
    print(max(d))
else:
    print(-1)