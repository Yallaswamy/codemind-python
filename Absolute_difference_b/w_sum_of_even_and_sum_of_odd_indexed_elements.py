n=int(input())
a=list(map(int,input().split()))
s=s1=0
import math
for i in range(n):
    if(i%2==0):
        s=s+a[i]
for i in range(n):
    if(i%2!=0):
        s1=s1+a[i]
print(abs(s-s1))