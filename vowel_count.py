n=input().lower()
a="aeiou"
c=0
for i in n:
    if(i in a):
        c=c+1
print(c)