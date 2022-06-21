n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ci=set(a)
d=set(b)
c=0
for i in ci:
     if i not in d:
         c=c+1
for i in d:
    if i not in ci:
        c=c+1
print(c)