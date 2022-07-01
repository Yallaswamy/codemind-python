n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
for i in a:
    if i>=b and i<=c:
        continue
    else:
       d.append(i)
if(d==[]):
    print(-1)
else:
    print(*d)