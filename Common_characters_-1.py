n=input()
n=n.lower()
n=n.split()
r=n[0]
res=""
for i in r:
    for j in n:
        if(i not in j):
            break
    else:
        res+=i
if(len(res)!=0):
    print(res)
else:
    print(-1)