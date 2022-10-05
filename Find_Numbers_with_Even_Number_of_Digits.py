n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(i)
    if(len(j)%2==0):
        c=c+1
print(c)