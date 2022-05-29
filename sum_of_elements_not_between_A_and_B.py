n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
sum=0
for i in a:
    if(i not in range(x,y+1)):
        sum=sum+i
print(sum)