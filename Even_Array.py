n=int(input())
a=list(map(int,input().split()))
k=len(a)
f=0
for i in a:
    if(i%2==0):
        f=f+1
if(k==f):
    print(True)
else:
    print(False)
        