n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=[]
for i in a:
    for j  in b:
        if i==j not in e :
            e.append(i)
print(*(e))