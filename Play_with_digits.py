n=int(input())
a=list(map(int,input().split()))
sum=0
r=0
for i in a:
    if(i<=9):
        sum+=i
    else:
        while(i!=0):
            r=i%10
            sum+=r
           # print(sum)
            i=i//10
print(sum)
