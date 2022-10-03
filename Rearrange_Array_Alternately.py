for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=n//2
    if(n%2==0):
        for i in range((n//2)):
            if(i<m-1):
                print(a[n-1-i],a[i],end=" ")
            else:
                print(a[n-1-i],a[i],end="")
    else:
        for i in range(n//2):
            print(a[n-1-i],a[i],end=" ")
        print(a[m],end="")
    print()