n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
s=s1=0
for i in range(n):
    for j in range(m):
        if(i%2==0):
            s=s+a[i][j]
        else:
            s1=s1+a[i][j]
print(s,s1)