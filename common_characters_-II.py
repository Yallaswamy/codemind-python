n=input()
n=n.lower()
s=input()
s=s.lower()
q=""
for i in n:
    if i  in s and i not in q and i!=' ':
        q+=i
for i in s:
    if i  in n and i not in q and i!=' ':
        q+=i
print(len(q))