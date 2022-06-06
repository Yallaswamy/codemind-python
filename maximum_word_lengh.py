n=input()
m=n.split()
c=0
k=0
#print(m)
for i in n:
    if(i==" "):
        k=c
        c=0
    else:
        c=c+1
for i in n:
    if n in m:
        print(c)
        break
    else:
        if(k>c):
            print(k)
            break
        else:
            print(c)
            break

