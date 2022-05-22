n=int(input())
i=0
j=0
f=1
for i in range(1,n+1):
    f=1
    m=int(input())
   # print("m=",m)
    for j in range(1,m+1):
        f=f*j
       # print(j)
    print(f)