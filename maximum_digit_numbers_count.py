n=input()
c=list(map(int,input().split()))
#print(c)
d=0
m=0
for i in c:
    if(i<0):
       # i=i*(-1)
        k=len(str(i))
        if(k>m):
            m=k
    else:
         k=len(str(i))
        # print(k)
         if(k>d):
             d=k
#print(m)
for i in c:
    k=len(str(i))
    if(d==k):
        print(i,end=" ")
    else:
        if(m>d):
            if(m==k):
                print(i,end=" ")
        

