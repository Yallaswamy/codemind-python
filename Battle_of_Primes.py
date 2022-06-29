def prime(n):
    count=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            count+=1
    if count==0:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
s=a+b
i=1
while(1):
    if(prime(s+i)):
        print(i)
        break
    i=i+1