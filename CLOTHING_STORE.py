n=int(input())
p=list(map(int,input().split()))
c=0
k=0
for i in range(n):
    c=1
    if(p[i]!=-1):
        for j in range(n):
            if(p[j]==p[i] and i!=j):
                c+=1
                p[j]=-1
        k+=c//2
print(k)