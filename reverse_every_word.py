n=input()
m=n.split()
y=[]
for i in m:
    y.append(i[::-1])
c=" ".join(y)
print(c)