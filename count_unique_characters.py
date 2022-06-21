n=input()
n=n.split()
n="".join(n)
n=n.lower()
n=sorted(n)
c=0
for i in n:
    if(n.count(i)==1):
        c=c+1
print(c)
