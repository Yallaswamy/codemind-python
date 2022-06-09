n=input()
v="0123456789"
c=0
for i in n:
    if(i in v):
       # print(i)
        c=c+int(i)
print(c)