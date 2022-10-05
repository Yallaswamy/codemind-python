for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(k):
        temp1=a[0]
        a[0]=a[-1]
        for j in range(1,n):
            temp2=a[j]
            a[j]=temp1
            temp1=temp2
    print(*a)

        
        