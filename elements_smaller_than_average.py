n=int(input())
a=list(map(int,input().split()))
b=sum(a)
av=b//n
c=0
for i in a:
    if(i<=av):
        c=c+1
print(c)