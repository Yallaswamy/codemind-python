n=int(input())
sum=0
r=0
m=n
while(n!=0):
    r=n%10
    f=1
    for i in range(1,r+1):
        f=f*i
    #print(f)
    sum=sum+f
    n=n//10
if(sum==m):
    print("The number",m,"is a strong number")
else:
    print("The number",m,"is not a strong number")