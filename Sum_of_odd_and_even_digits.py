n=int(input())
x=y=0
a=list(map(int,input().split()))
for i in range(n):
    if(i%2==0):
        x+=a[i]
    else:
        y+=a[i]
if(abs(x-y)==0):
    print("YES")
else:
    print("NO")