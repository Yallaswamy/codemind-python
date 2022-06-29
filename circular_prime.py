##twisted prime

n=int(input())
k=0
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        print("not prime")
        k=1
        break
else:
    m=n
    #print(m)
    r=0
    rev=0
    while m:
        r=m%10
        #print(r)
        rev=rev*10+r
        m=m//10
    #print(rev)
    o=rev
    s=0
    for j in range (2,int(o**0.5)+1):
        if(o%j==0):
            s=1
            print("prime but not a circular prime")
            break
    if(s==0):
        print("circular prime")

        

        
        
