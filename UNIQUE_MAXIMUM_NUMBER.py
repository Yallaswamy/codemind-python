n=int(input())
c=0
b=[]
a=list(map(int,input().split()))
for i in a:
    if(a.count(i)==1):
        b.append(i)
        c=1
if(c==0):
    print(-1)
else:
    print(max(b))