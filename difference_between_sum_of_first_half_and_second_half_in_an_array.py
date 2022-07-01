n=int(input())
a=list(map(int,input().split()))
#print(a)
c=c1=0
for i in range(0,n//2):
    c=c+a[i]
#print(c)
for i in range(n//2,n):
    c1=c1+a[i]
print(abs(c-c1))