n=int(input())
a=0
b=1
f=0
print(a,b,end=" ")
for  i in range (3,n+1):
    f=a+b
    print(f,end=" ")
    a=b
    b=f
    