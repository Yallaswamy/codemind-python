n=input()
v=int(input())
d=c=0
for i in range(len(n)):
    if n[i]=='a':
        d+=1
res=v//len(n)*d
v=v%len(n)
for i in range(v):
    if n[i]=='a':
        c+=1
print(c+res)