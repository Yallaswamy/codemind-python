n=input()
n=n.split()
n="".join(n)
n=n.lower()
n=sorted(n)
b=[]

for i in n:
    if(i not in b):
        b.append(i)
        print(i,end="")

    
    
        


