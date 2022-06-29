n,m=map(int,input().split())
k=[]
for i in range(n):
    a=list(map(int,input().split()))
    k.append(a)
c=0
for i in range(n):
   # print(k[i])
    #print(sorted(k[i]))
    #print(k[i][::-1])
   # print(k[::-1][i])
    if(sorted(k[i])==(k[i]) or k[i][::-1]==sorted(k[i])):
        c=c+1
print(c)