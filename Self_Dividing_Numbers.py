a=int(input())
b=int(input())
for n in range(a,b+1):
    m=n
    c=0
    f=0
    while(n!=0):
        r=n%10
        c=c+1
        if(r!=0):
            if(m%r==0):
                f=f+1
        n=n//10
    if(c==f):
        print(m,end=" ")
    