n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=f=0
    for j in range(i+1,n):
        if(a[j]>a[i]):
            print(c+1,end=" ")
            f=1
            break
        else:
            c=c+1
    if(f==0):
        print("0",end=" ")