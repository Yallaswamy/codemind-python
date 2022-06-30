n=int(input())
a=list(map(int,input().split()))
x=int(input())
f=0
for i in a:
    if(x in a):
        f=1
    else:
        f=0
if(f==1):
    print(True)
else:
    print(False)