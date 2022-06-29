n=int(input())
a=[]
for i in str(n):
    a.append(int(i))
for i in range(len(a)):
    if(a[i]==6):
        a[i]=9
        break
for i in range(len(a)):
    print(a[i],end="")