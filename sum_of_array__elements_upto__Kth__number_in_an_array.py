n=int(input())
a=list(map(int,input().split()))
x=int(input())
sum=0
for i in a:
    if i in range(x+1):
        sum=sum+i
print(sum)