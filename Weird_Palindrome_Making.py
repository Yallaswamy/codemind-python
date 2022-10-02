for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(a[i]%2!=0):
            c+=1
    print(c//2)
