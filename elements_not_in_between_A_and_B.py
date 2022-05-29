n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
sum=0
f=0
for i in a:
    if(i not in range(x,y+1)):
       f=f+1
       print(i,end=" ")
if(f==0):
    print("-1")
    