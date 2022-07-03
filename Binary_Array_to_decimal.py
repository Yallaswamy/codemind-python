n=int(input())
a=list(map(int,input().split()))
s=0
b=0
for i in a[::-1]:
    s=s+(i*2**b)
   # print(s)
    b=b+1
print(s)
    
    