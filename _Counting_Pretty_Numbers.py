t=int(input())
for i in range(0,t):
    n,m=map(int,(input().split()))
    c=0
    r=0
    for i in range(n,m+1):
        k=l=i
        if(k<=9):
            #print(k)
            if(k==2 or k==3 or k==9):
                c=c+1
        else:
             r=l%10
             if(r==2 or r==3 or r==9):
                   c=c+1
    print(c)
