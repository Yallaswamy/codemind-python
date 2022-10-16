n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-2):
    if(a[i+2]==a[i]+a[i+1]):
        c=1
    else:
        c=0
        break

if(c==1):
    print("yes")
else:
    print("no")