s1=input().lower()
s2=input().lower()
a=[]
for i in s1:
    if(i in s2  and i not in a and i!=" "):
        a.append(i)
x="".join(sorted(a))
if(len(a)!=0):
    print(x)
else:
    print(-1)