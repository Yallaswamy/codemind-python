n=int(input())
a=list(map(int,input().split()))
t=int(input())
b=[]
for i in range(n):
    if(a[i]==t):
        b.append(i)
if(len(b)!=0):
    print(min(b),max(b))
else:
    print(-1,-1)