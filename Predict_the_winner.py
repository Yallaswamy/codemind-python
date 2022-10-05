n=int(input())
x=y=0
a=list(map(int,input().split()))
#print(a)
for i in range(n//2):
    x+=a[i]
for j in range(n//2,n):
    #print(a[j])
    y+=a[j]
#print(x,y)
d=abs(x-y)
if(d%4==0):
    print("X")
else:
    print("Y")