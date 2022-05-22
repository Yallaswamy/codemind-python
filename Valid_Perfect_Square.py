n=int(input())
p=0
for i in range(1,n+1):
    m=int(input())
    k=m**(1/2)
    q=int(k)
   # print(q,k)
    if(q==k):
        print(True)
    else:
        print(False)