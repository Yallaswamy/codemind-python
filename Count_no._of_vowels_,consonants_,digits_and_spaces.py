n=input()
n=n.lower()
c,v,w,d=0,0,0,0
a="aeiou"
b="bcdfghjklmnpqrstvwxyz"
for i in n:
    if(i in a):
        v=v+1
    elif i in b:
        c=c+1
    elif ord(i)==32:
        w=w+1
    elif i.isdigit():
        d=d+1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)
    
        