def prime(n):
    c=0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            c=c+1
    if(c==0):
        return 1
    else:
        return 0
n=int(input())
n1=int(input())
s=n+n1
i=1
while(1):
    if(prime(s+i)):
        print(i)
        break
    i=i+1

        
