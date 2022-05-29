n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
sum=0
for i in a:
    f=0
    if(max(a) not in range(x,y+1)):
       f=f+1
       print(max(a))
       break
if(f==0):
    print("-1")