n=input().lower()
n=n.split()
a="aeiou"
ma=100
for i in n:
    c=0
    for j in i:
        if(j in a):
            c=c+1
    if(c<ma):
        ma=c
print(ma)
    
            