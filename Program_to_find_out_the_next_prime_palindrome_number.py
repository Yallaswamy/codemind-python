def pal(n):
    s=n
    rev=0
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if(s==rev):
        return 1
    else:
        return 0
def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        else:
            return 1
        
n=int(input())
for i in range(n+1,100000):
    if(pal(i)):
        if(prime(i)):
            print(i)
            break
            