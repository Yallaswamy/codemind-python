n=int(input())
f=0
sum=0
a=list(map(int,input().split()))
for i in a:
    sum=sum+i
for i in a:
    if(i==(sum//n)):
        f=1
        break
    else:
        f=0
if(f==1):
    print(True)
else:
    print(False)