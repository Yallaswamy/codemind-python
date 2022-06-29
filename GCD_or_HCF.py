n,n1=map(int,input().split())
k=max(n,n1)
gcd=0
for i in range(1,k):
    if(n%i==0 and n1%i==0):#4 6 i=2
        gcd=i
print(gcd)
