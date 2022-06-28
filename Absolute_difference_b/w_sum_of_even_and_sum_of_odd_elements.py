n=int(input())
import math
a=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if(a[i]%2!=0):
        s=s+a[i]
for i in range(n):
    if(a[i]%2==0):
        s1=s1+a[i]
print(abs(s1-s))