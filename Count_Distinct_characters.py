n=input()
n=n.split()
n="".join(n)
n=n.lower()
#n=sorted(n)
b=[]
c=0
for i in n:
    if(i not in b):
        b.append(i)
        c=c+1
print(c)
    
    
        


