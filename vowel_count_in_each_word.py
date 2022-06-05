n=input()
#print(n)
v="AEiOUaeiou"
c=0
for  i in n:
    if(i in v and i!=" "):
        c=c+1
    if(i==" "):
        print(c,end=" ")
        c=0
print(c,end=" ")