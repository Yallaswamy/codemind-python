n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(n):
    s=(s*10)+a[i]
s=s+1
#print(s)
b=[]
while(s>0):
    r=s%10
    b.append(r)
    s=s//10
c=reversed(b)
print(*c)