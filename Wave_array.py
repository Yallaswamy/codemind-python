n=int(input())
a=list(map(int,input().split()))
c=0

for i in range(0,n-1,2):
    if(a[0]<a[1]):
        if(a[i]<a[i+1]):
            c=c+1
    else:
        if(a[i]>a[i+1]):
           c=c+1
        
if(c==n//2):
    print("yes")
else:
    print("no")
        
    