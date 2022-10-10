n=input().lower()
n=n.split()
a="aeiou"
ma=100
e=0
for i in n:
    c=0
    for j in i:
        if(j in a):
            c=c+1
    if(c<ma):
        ma=c
for i in n:
    c=0
    for j in i:
        if(j in a):
            c=c+1
    if(ma==c):
        e=e+1
print(e)
    
            