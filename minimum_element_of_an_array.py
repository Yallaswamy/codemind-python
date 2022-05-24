n=int(input()) 
a=list(map(int,input().split()))
max=0
min=a[0]
for i in range (1,n):#for i in a:
    if(a[i]<min):    #if i<m:
        min=a[i]     #m=i
print(min)
