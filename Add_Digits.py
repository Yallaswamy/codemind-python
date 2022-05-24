def adddigits(n):
    sum=0
    r=0
    while(n!=0):
        r=n%10
        sum=sum+r
        n=n//10
    return sum
        
n=int(input())
#print(n)
k=adddigits(n)
#print(k)
for i in range(0,10):
    if(k==i):
        print(i)
        break
else:
    k=adddigits(k)
    s=0
    while(k!=0):
        m=k%10
        s=s+m
        k=k//10
    print(s)


