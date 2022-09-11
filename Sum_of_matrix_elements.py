n=int(input())
m=int(input())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    #for j in range()
    a.append(b)
#print(a)
s=0
ma=0
for i in range(n):
    for j in range(m):
        s=s+a[i][j]
print(s)