n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=[]
for i in a:
     if i not in b:
         e.append(i)
for i in b:
    if i not in a:
        e.append(i)
print(*e)