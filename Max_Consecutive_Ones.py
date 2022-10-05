n=int(input())
a=list(map(int,input().split()))
c=0
ma=0
for i in a:
    if(i==1):
        c+=1
    if(ma<c):
        ma=c
    if(i==0):
        c=0
if(ma>c):
    print(ma)
else:
    print(c)