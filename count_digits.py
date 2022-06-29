n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if(i<0):
        i=i*-1
        b=len(str(i))
        c.append(b)
    else:
        b=len(str(i))
        c.append(b)
        
print(*c)