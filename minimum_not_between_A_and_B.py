n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=[]
e=[]
for i in a:
    if(i>=b and i<=c):
        d.append(i)
    else:
        e.append(i)
if e==[]:
    print(-1)
else:
    print(min(e))
