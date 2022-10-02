a=int(input())
b=int(input())
sum=0
ar=0
for i in range(a,b+1):
    sum=0
    for j in range(i,b+1):
        sum+=j
        if sum%2!=0:
            ar+=1
print(ar)
        
    