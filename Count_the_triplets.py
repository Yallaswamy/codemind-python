for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        sum=0
        for j in range(i+1,n):
            sum=a[i]+a[j]
            if(sum in a):
                c=c+1
                sum=0
            else:
                sum=0
    if(c==0):
        print("-1")
    else:
        print(c)
                