n=input()
k=""
c=0
c1=0
for i in n:
    if(i!=" "):
        k+=i
x=min(k)
y=max(k)
for i in k:
    if(i==x):
        c=c+1
    if(i==y):
        c1+=1
print(x,c,y,c1)