n=input()
k="aeiou"
c=0
b=[]
for i in k:
    if i not in n:
        b.append(i)
        c=c+1
if(c>0):
    print(*b)
else:
    print(0)
        