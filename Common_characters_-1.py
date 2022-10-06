s1=input().lower()
s1=s1.split()
r=s1[0]
res=[]
for i in r:
    for j in s1:
        if i not in j:
            break
    else:
        res.append(i)
x="".join(res)
if(len(res)==0):
    print(-1)
else:
    print(x)