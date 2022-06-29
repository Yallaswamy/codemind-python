n=int(input())
m=int(input())
s=s1=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
#print(s)
for i in range(1,m):
    if(m%i==0):
        s1=s1+i
#print(s1)
if(n==s1 and s==m):
    print("Amicable")
else:
    print("Not Amicable")