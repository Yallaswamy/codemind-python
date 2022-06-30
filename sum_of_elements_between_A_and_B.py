n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
d=[]
s=0
for i in m:
    if(i in range(a,b+1)):
        d.append(i)
for i in d:
    s=s+i
print(s)