n=input()
n=n.lower()
c=0
for i in n:
    if(n.count(i)==1 and i!=" "):
        c=c+1
print(c)