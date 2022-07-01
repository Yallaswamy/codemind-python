n=int(input())
a=list(map(int,input().split()))
s=c=0
b=[]
for i in a:
    if(a.count(i)==i and i not in b):
        b.append(i)
        s=s+i
        c=c+1
if(c==0):
    print(-1)
else:
    av=s/c
    print("{:.2f}".format(av))
    