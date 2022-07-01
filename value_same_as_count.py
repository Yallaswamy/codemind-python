n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if(a.count(i)==i and i not in b):
        c=c+1
        b.append(i)
print(c)