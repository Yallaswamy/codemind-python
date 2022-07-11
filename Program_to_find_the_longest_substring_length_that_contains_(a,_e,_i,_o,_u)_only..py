n=input()
n=n.lower()
c=0
ma=0
a="aeiou"
for i in n:
    if i in a:
        c=c+1
        if(c>ma):
            ma=c
    else:
        c=0
print(ma)

        