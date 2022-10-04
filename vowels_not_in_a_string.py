n=input().lower()
a="aeiou"
b=""
c=0
for i in n:
    if(i in a):
        b+=i
for i in a:
    if(i not in b):
        print(i,end=" ")
        c=1
if(c==0):
    print(0)

        