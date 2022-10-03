n=input()
n=n.lower()
a=[]
for i in n:
    if(n.count(i)==1 and i!=" "):
        a.append(i)
a=sorted(a)
a="".join(a)
print(a)