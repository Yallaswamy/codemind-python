n=int(input())
m=n*n
r=m%10
t=m%100
s=m%1000
if(n==r or t==n or s==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")