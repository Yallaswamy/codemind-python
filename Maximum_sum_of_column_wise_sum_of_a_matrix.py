n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
s=0
ma=0
for j in range(m):
    for i in range(n):
        s=s+a[i][j]
    if(s>ma):
        ma=s
    s=0
print(ma)
