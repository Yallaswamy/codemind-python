n=int(input())
a=list(map(int,input().split()))
c=c1=0
for i in range(0,n//2):
    c=c+a[i]
for i in range(n//2,n):
    c1+=a[i]
print(c)
print(c1)