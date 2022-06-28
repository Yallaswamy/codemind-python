n=int(input())
a=[]
for i in range(1,n+1):
    if(n%i==0):
        a.append(i)
def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
c=0
for i in range(len(a)):
    if(prime(a[i])):
        continue
    else:
        c=c+1
print(c)