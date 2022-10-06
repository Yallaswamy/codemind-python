s1=input().lower()
s2=input().lower()
a=[]
for i in s1:
    if(i not in s2 and i!=" "):
        a.append(i)
for i in s2:
    if(i not in s1 and i!=" "):
        a.append(i)
a=set(a)
x="".join(sorted(a))
print(x)