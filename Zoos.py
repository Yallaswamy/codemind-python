n=input()
a="z"
b="o"
c=c1=0
for i in n:
    if i in a:
        c=c+1
    else:
        c1=c1+1
#print(c,c1)
if(2*c==c1):
    print("Yes")
else:
    print("No")