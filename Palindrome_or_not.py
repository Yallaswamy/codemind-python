n=input()
#print(n)
n=n.lower()
n=n.split()
for i in n:
    m=i
    p=i[::-1]
    if(m==p):
        print(True)
    else:
        print(False)
