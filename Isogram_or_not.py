n=input()
c=0
x=len(n)
for i in n:
    if(n.count(i)==1):
        c=c+1
if(x==c):
    print(True)
else:
    print(False)
        