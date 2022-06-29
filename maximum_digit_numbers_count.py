n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
p=0
for i in a:
    b=len(str(i))
    c.append(b)
for i in a:
    if(max(c)==len(str(i))):
        print(i,end=" ")