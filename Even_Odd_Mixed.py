n=int(input())
f=0
c=0
while(n!=0):
    r=n%10
    if(r%2==0):
        f=1
    elif(r%2!=0):
        c=1
    n=n//10
if(f>=1 and c>=1):
    print("Mixed")
elif(f>=1):
    print("Even")
elif(c>=1):
    print("Odd")