n=input()
c=list(map(int,input().split()))
#print(c)
d=0
m=100
n=0
for i in c:
    k=len(str(i))
    if(m>k):
        m=k
for i in c:
    k=len(str(i))
    if(m==k):
        n=n+1
print(n)
        

