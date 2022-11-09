def rev(n):
    n=n[::-1]
    return n
n=input()
n=n.split()
a=[]
for i in range(len(n)):
    if(i%2==0):
        k=rev(n[i])
        a.append(k)
    else:
        a.append(n[i])
    
print(*a)