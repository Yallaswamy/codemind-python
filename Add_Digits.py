def digit(n):
    res=0
    while(n!=0):
        r=n%10
        res=res+r
        n=n//10
    if(res>9):
        return digit(res)
    else:
        return res
n=int(input())
k=digit(n)
print(k)