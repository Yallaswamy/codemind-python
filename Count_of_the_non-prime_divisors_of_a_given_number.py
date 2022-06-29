def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
n=int(input())
b=[]
c=0
for i in range(1,n+1):
    if(n%i==0):
        b.append(i)
for i in b:
    if(prime(i)):
        c=c+1
print(len(b)-c)