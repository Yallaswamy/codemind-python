n=int(input())
a=list(map(int,input().split()))
b=set(a)
sum=0
for i in b:
    if(i%2==0):
        sum=sum+i
print(sum)