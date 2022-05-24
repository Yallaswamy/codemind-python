n=int(input())
a=list(map(int,input().split()))
#print(a)
f=0
for i in range(0,n):
    if(a[i]<n):
        f=1
    else:
        f=0
        break
if(f==1):
    print("YES")
else:
    print("NO")
        