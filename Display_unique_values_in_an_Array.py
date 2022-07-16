n=int(input())
a=list(map(int,input().split()))
b=[]
c=0
for i in a:
    if a.count(i)==1:
        b.append(i)
        c=1
if(c==1):
    print(*b)
else:
    print(-1)