def rev(n):
    re=0
    while(n!=0):
        r=n%10
        re=re*10+r
       # print(re)
        n=n//10
    #print(re)
    return re
n=int(input())
b=list(map(int,input().split()))
a=[]
for i in b:
    k=rev(i)
   # print(k)
    a.append(k)
print(*a)