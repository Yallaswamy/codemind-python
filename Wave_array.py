n=int(input())
a=list(map(int,input().split()))
#print(a)
c=0
d=0
for i in range(0,n-1,2):
    if(a[i]>a[i+1]):
        c=c+1
for i in range(0,n-1,2):
    if(a[i]<a[i+1]):
        d=d+1

#print(c,d)
if(c==n//2 or d==n//2):
    print("yes")
else:
    print("no")