n=input()
m=input()
n=n.lower()
m=m.lower()
for i in m.split():
    if( i in n.split()):
        print(i,end=" ")