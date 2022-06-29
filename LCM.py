def lcm(a,b):
     c=max(a,b)
     while 1:
        if(c%a==0 and c%b==0):##3 4 c=12
            return c
        c=c+1
a,b=map(int,input().split())
print(lcm(a,b))
