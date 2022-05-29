n=int(input())
a=list(map(int,input().split()))
sum=0
c=0
#print(a)
for i in a:
    sum=sum+i
k=int(sum/n)
for i in a:
    if(i>=k):
        c=c+1
print(c)
