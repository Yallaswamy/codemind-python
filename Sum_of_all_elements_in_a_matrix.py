n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
s=s1=0
for i in range(n):
    for j in range(m):
            s=s+a[i][j] 
print(s)