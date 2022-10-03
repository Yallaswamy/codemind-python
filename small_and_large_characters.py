n=input()
n=n.split()
q=""
x=0
y=0
for i in n:
    x=min(i)
    y=max(i)
    print(x,y,end=" ")