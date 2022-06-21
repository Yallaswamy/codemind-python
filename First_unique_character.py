n=input()
n=n.split()
n="".join(n)
n=n.lower()
for i in n:
    if(n.count(i)==1):
        print(i)
        break
else:
    print(-1)

