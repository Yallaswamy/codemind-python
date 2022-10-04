n=input()
a="aeiou"
n=set(n)
n=list(n)
c=0
for i in n:
    if( i in a):
        c=c+1
if(c==5):
    print(True)
else:
    print(False)
