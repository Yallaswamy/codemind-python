n=int(input())
r=0
sum=0
m=n
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
if(m%sum==0):
    print("True")
else:
    print(False)
    
