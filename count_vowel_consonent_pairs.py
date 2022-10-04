n=input().lower()
n=list(n)
v="aeiou"
c="bcdfghjklmnpqrstvwxyz"
c1=0
for i in range(len(n)):
    if((n[i] in v and n[len(n)-1-i] in c) or (n[i] in c and n[len(n)-1-i] in v)):
        c1=c1+1
print(c1//2)
        