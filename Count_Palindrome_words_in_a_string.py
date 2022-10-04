n=input().lower()
n=n.split()
c=0
n=list(n)
for i in n:
    if(i==i[::-1]):
        c=c+1
print(c)
