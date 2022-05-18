n=int(input())

c=0
t=n
for i in range(1,10):
    f=0
    t=n
    
    while t!=0:
        #print(i)
        r=t%10
        #print(i)
        if(r==i):
            f=f+1
        #print(f,i)
        t=t//10
        #print(i)
    if(f>1):
        c=c+1
#print(i)
if(c==0):
    print("Unique Number")
else:
    print("Not Unique Number")
        #