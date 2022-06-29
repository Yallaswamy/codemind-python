n=int(input())
a=list(map(int,input().split()))
#print(a)
c=[]
p=0
for i in a:
    b=len(str(i))
    c.append(b)
for i in a:
    if(min(c)==len(str(i))):
        p=p+1
print(p)
    

