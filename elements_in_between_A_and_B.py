n=int(input())
a=list(map(int,input().split()))
#print(a)
x,y=map(int,input().split())
#print(x,y)
b=[]
c=0
for i in a:
    if i in range(x,y+1):
        b.append(i)
        c=c+1
#print(b)
if(c==0):
    print(-1)
else:
    print(*b)