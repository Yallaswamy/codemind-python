n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
c=s//n
if(c in a):
    print(True)
else:
    print(False)