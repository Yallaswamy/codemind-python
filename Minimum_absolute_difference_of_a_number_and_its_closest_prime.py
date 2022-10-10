def prime(n):
    if(n>1):
        for i in range(2,int(n**0.5)+1):
            if(n%i==0):
                return 0
        return 1
a=int(input())
c=df=vf=0
for i in range(a,0,-1):
    if prime(i)==1:
        f=i
        df=a-f
        break
for j in range(a,10000):
    if prime(j)==1:
        g=j
        vf=g-a
        break
if df==vf:
    print(df)
elif df>vf:
    print(vf)
else:
    print(df)
    
    