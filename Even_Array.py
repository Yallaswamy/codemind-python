n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if( i%2==0):
        c=c+1
if(n==c):
    print(True)
else:
    print(False)
