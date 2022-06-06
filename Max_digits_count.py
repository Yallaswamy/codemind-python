n=input()
c=list(map(int,input().split()))
#print(c)
d=0
m=0
n=0
for i in c:
    k=len(str(i))
    if(k>m):
        m=k
for i in c:
    k=len(str(i))
    if(m==k):
        n=n+1
print(n)
        

