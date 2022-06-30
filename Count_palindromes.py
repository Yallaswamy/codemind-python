def pal(n):
    t=n
    re=0
    while(t!=0):
        r=t%10
        re=re*10+r
        t=t//10
    if(n==re):
        return 1
    return 0
n=int(input())
c=0
a=list(map(int,input().split()))
for i in a:
    if(pal(i)):
        c=c+1
print(c)
