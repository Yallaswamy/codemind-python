a=list(map(int,input().split(",")))
#print(a)
b=[]
for i in a:
    sum=0
    for j in range(1,i+1):
        if(i%j==0):
            sum+=j
    if sum in a:
        b.append(i)
if(len(b)!=0):
    b=sorted(b)
    print(*b)
else:
    print(-1)