def prime(n):
    if(n>1):
        for i in range(2,int(n**(0.5))+1):
            if(n%i==0):
                return 0
        return 1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
#print(k)
c=0
for i in a:
    if(i<=k):
        if(prime(i)):
            c=c+1
print(c)