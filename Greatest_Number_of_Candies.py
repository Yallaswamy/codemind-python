n=int(input())
a=list(map(int,input().split()))
t=int(input())
m=max(a)
for i in range(n):
    if(((a[i]+t))>=m):
        print(True,end=" ")
    else:
        print(False,end=" ")
    