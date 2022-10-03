for i in range(int(input())):
    a,t=map(int,input().split())
    l=list(map(int,input().split()))
    k=m=c=0
    for i in range(a):
        s=0
        for j in range(i,a):
            s+=l[j]
            if(s==t):
                k=i
                m=j
                c=1
                break
        if(c==1):
            break
    if(c==1):
        print(k+1,end=" ")
        print(m+1)
    else:
        print(-1)
                