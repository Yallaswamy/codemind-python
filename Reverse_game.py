n=int(input())
a=list(map(int,input().split()))
rev=0
for i in a:
    rev=0
    while(i!=0):
        r=i%10
        rev=rev*10+r
        i=i//10
        if(i==0):
            print(rev,end=" ")
        
