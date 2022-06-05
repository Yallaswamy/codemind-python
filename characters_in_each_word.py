n=input()
#print(n)
c=0
for i in range(len(n)):
    c=c+1
    if(n[i]==" "):
        print(c-1,end=" ")
        c=0
print(c,end=" ")